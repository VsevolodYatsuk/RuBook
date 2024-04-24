using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace rubook_backend.Migrations
{
    /// <inheritdoc />
    public partial class ddreatedateolumn : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<string>(
                name: "CreatedDate",
                table: "Books",
                type: "TEXT",
                nullable: true);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "CreatedDate",
                table: "Books");
        }
    }
}
