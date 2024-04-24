using System.ComponentModel.DataAnnotations;

public class Book
{
    public int Id { get; set; }
    
    [Required]
    public string? Title { get; set; }
    
    [Required]
    public string? Author { get; set; } 
    
    public string? Genre { get; set; } 
    
    public int Year { get; set; } 
    
    public decimal Price { get; set; } 
    
    public string? PhotoUrl { get; set; } 
    
    public string? Description { get; set; }
    
    public string? CreatedDate { get; set; }
}
