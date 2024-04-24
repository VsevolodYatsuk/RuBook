using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System.Threading.Tasks;

[Route("api/admin")]
[ApiController]
public class AdminController : ControllerBase
{
    private readonly AppDbContext _context;

    public AdminController(AppDbContext context)
    {
        _context = context;
    }

    [HttpPost("login")]
    public async Task<ActionResult<Admin>> Login(Admin request)
    {
        var admin = await _context.Admins.FirstOrDefaultAsync(a => a.Username == request.Username && a.Password == request.Password);

        if (admin == null)
        {
            return NotFound("Invalid username or password");
        }

        return Ok(admin);
    }
}
