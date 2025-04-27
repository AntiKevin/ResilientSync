from click import echo, group, option, style


@group()
def cli():
    """
    A command-line interface for uploading files to nextcloud.
    """
    pass

@cli.command('upload', short_help='Upload a file to the server.')
@option('--file', type=str, help='Path to the file to upload.', required=True)
@option('--destination', type=str, help='Destination path on the server.', required=True)
@option('--overwrite', is_flag=True, help='Overwrite the file if it exists.', default=False)
def upload(file: str, destination: str, overwrite: bool):
    """
    Uploads a file to the server.
    """
    echo(style(f'Uploading {file} to {destination}...', fg='green'))
    echo(style('Upload complete!', fg='green'))
    echo(f'Overwrite: {overwrite}')





if __name__ == '__main__':
    cli()