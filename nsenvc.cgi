#!/usr/bin/perl
# =====================================================================
# $Id: nsenvc.cgi,v1.0 - 09/12/2016 22:35 - J. L. Freimam         Exp $
# =====================================================================

use strict;
my $copyright = '2016 &copy;';
my $program_name = 'NSENVC';
my $ver = '1.0';

my $is_sendmail = 'Cannot locate sendmail';

my @send_mail = qw(
    /usr/sbin/sendmail
    /sbin/sendmail
    /usr/bin/sendmail
    /bin/sendmail
    /usr/lib/sendmail
    /lib/sendmail
    /usr/slib/sendmail
    /slib/sendmail
    /usr/sendmail
    /sendmail
    sendmail
    /var/qmail/bin/qmail-inject
    );

eval { require 5 };
my $is_perl = $@ ? 'No' : 'Yes';
my $perl_version = $];

eval { require CGI };
my $is_cgi = $@ ? 'No' : 'Yes';
my $cgi_version = $CGI::VERSION;

my $script = $0;
$script =~ s/.*\/(.*?)/$1/;

my $gateway_interface = $ENV{'GATEWAY_INTERFACE'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $document_root = $ENV{'DOCUMENT_ROOT'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $context_document_root = $ENV{'CONTEXT_DOCUMENT_ROOT'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $http_host = $ENV{'HTTP_HOST'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $http_user_agent = $ENV{'HTTP_USER_AGENT'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $script_name = $ENV{'SCRIPT_NAME'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $script_filename = $ENV{'SCRIPT_FILENAME'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $string = $ENV{'QUERY_STRING'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $prefix = $ENV{'CONTEXT_PREFIX'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $remote_addr = $ENV{'REMOTE_ADDR'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $http_accept = $ENV{'HTTP_ACCEPT'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $http_accept_encoding = $ENV{'HTTP_ACCEPT_ENCODING'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $http_accept_language = $ENV{'HTTP_ACCEPT_LANGUAGE'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $http_connection = $ENV{'HTTP_CONNECTION'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $http_dnt = $ENV{'HTTP_DNT'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $remote_port = $ENV{'REMOTE_PORT'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $request_method = $ENV{'REQUEST_METHOD'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $request_scheme = $ENV{'REQUEST_SCHEME'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $server_addr = $ENV{'SERVER_ADDR'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $server_port = $ENV{'SERVER_PORT'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $server_admin = $ENV{'SERVER_ADMIN'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $server_name = $ENV{'SERVER_NAME'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $server_protocol = $ENV{'SERVER_PROTOCOL'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $server_signature = $ENV{'SERVER_SIGNATURE'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $server_software = $ENV{'SERVER_SOFTWARE'};
if (eval { require Cwd; })
{
	use Cwd;
}

my $unique_id = $ENV{'UNIQUE_ID'};
if (eval { require Cwd; })
{
	use Cwd;
}

for (@send_mail) { $is_sendmail = $_ if (-e $_); }

print "Content-Type: text/html\n\n";
print <<HTML;
<!DOCTYPE HTML PUbLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd"> 
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="Program Name" content="$program_name">
<meta name="Version" content="$ver">
<title>Navscape Environment Checker</title>
<style rel="stylesheet" type="text/css">
	/*<![CDATA[*/
	html, body {color: #000; background-color: #fff; font-size:12px; font-family: Verdana, Arial, Helvetica, sans-serif;}
    table {width: 80%;}
    table td {padding: 0; border-width: 0; vertical-align: top; }
    table.center {margin-left:auto; margin-right:auto;  }
    /*]]>*/
</style>    
	
</head>

<body>
<table class="center" border="2" CELLSPACING="5">
  <tr>
    <td><font size="4"><b>Navscape Environment Checker</b></font></td>
  </tr>
</table>
<table class="center" border="2" CELLSPACING="5">
  <tr> 
    <td>Perl Version:</td>
    <td><b>$perl_version</b></td>
  </tr>
  <tr> 
    <td>CGI Version:</td>
    <td><b>$cgi_version</b></td>
  </tr>
  <tr> 
    <td>Gateway Interface:</td>
    <td><b>$gateway_interface</b></td>
  </tr>  
  <tr> 
    <td>Document Root:</td>
    <td><b>$document_root</b></td>
  </tr>
  <tr> 
    <td>CGI-BIN Document Root:</td>
    <td><b>$context_document_root</b></td>
  </tr>  
  <tr> 
    <td>Script File Name</td>
    <td><b>$script_filename</b></td>
  </tr>
  <tr> 
    <td>Script Name</td>
    <td><b>$script_name</b></td>
  </tr>
  <tr> 
    <td>Context Prefix:</td>
    <td><b>$prefix</b></td>
  </tr>
  <tr> 
    <td>HTTP Accept:</td>
    <td><b>$http_accept</b></td>
  </tr>
  <tr> 
    <td>HTTP Accept Encoding:</td>
    <td><b>$http_accept_encoding</b></td>
  </tr>
  <tr> 
    <td>HTTP Accept Language:</td>
    <td><b>$http_accept_language</b></td>
  </tr>
  <tr> 
    <td>HTTP Connection:</td>
    <td><b>$http_connection</b></td>
  </tr>
  <tr> 
    <td>HTTP DNT:</td>
    <td><b>$http_dnt</b></td>
  </tr>  
  <tr> 
    <td>HTTP Host:</td>
    <td><b>$http_host</b></td>
  </tr>
  <tr> 
    <td>HTTP User Agent:</td>
    <td><b>$http_user_agent</b></td>
  </tr>  
  <tr> 
    <td>Query String:</td>
    <td><b>[$string]</b></td>
  </tr>
    <tr> 
    <td>Remote Addr:</td>
    <td><b>$remote_addr</b></td>
  </tr>
    <tr> 
    <td>Remote Port:</td>
    <td><b>$remote_port</b></td>
  </tr>
  <tr> 
    <td>Request Method:</td>
    <td><b>$request_method</b></td>
  </tr>
  <tr> 
    <td>Request Scheme:</td>
    <td><b>$request_scheme</b></td>
  </tr>  
  <tr> 
    <td>Server Addr:</td>
    <td><b>$server_addr</b></td>
  </tr>
  <tr> 
    <td>Server Port:</td>
    <td><b>$server_port</b></td>
  </tr>  
  <tr> 
    <td>Server Admin:</td>
    <td><b>$server_admin</b></td>
  </tr>
  <tr> 
    <td>Server Name:</td>
    <td><b>$server_name</b></td>
  </tr>  
  <tr> 
    <td>Server Protocol:</td>
    <td><b>$server_protocol</b></td>
  </tr>
  <tr> 
    <td>Server Signature:</td>
    <td><b>$server_signature</b></td>
  </tr>
  <tr> 
    <td>Server Software:</td>
    <td><b>$server_software</b></td>
  </tr>
  <tr> 
    <td>Sendmail Path:</td>
    <td><b>$is_sendmail</b></td>
  </tr>  
  <tr> 
    <td>Unique ID:</td>
    <td><b>$unique_id</b></td>
  </tr>  
</table>
<center><p>$program_name $ver - Copyright $copyright Navscape</p></center>
</body>
</html>
HTML
exit;