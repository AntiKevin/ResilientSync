from click import echo, group, option, style


@group()
def cli():
    """
    A command-line interface for uploading files to nextcloud.
    """
    pass

@cli.group('nextcloud')
def nextcloud():
    """
    Commands for interacting with Nextcloud.
    """
    pass

@nextcloud.command('upload', short_help='Upload a file to the server.')
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

@nextcloud.command('login', short_help='Login to the server.')
@option('--url', type=str, help='URL of the server.', required=True)
@option('--username', type=str, help='Username for the server.', required=True)
@option('--password', type=str, help='Password for the server.', required=True)
def login(url: str, username: str, password: str):
    """
    Sing in to the server.
    """
    echo(style(f'Logging in to {url} as {username}...', fg='green'))

    echo(style('Login successful!', fg='green'))




if __name__ == '__main__':
    cli()