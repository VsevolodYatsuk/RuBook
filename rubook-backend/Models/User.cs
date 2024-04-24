using System.ComponentModel.DataAnnotations;

public class User
{
    public int Id { get; set; }

    [Required]
    public string? Email { get; set; }

    [Required]
    public string? Password { get; set; }

    [Required]
    public string? Login { get; set; }

    [Required]
    [Range(6, int.MaxValue, ErrorMessage = "Возраст больше 6 лет")]
    public int Age { get; set; }
}
