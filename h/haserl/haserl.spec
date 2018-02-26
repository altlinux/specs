Name: haserl
Version: 0.9.3
Release: alt2
License: GPL
Group: Development/Other
Source: %{name}-%{version}.tar.gz
Summary: Html And Shell Embedded Runtime Language

%description
haserl (Html And Shell Embedded Runtime Language) is a cgi
program that runs interpreted scripts.   It combines three
elements into a single CGI interpreter:

1. It parses POST and GET requests, placing form-elements as name=value
pairs into the environment for the CGI script to use. It is similar
to uncgi (http://www.midwinter.com/~koreth/uncgi.html) in this respect

2. It prints the contents of the script as html, and conditionally
interpets text within <? ... ?> as shell script.  In this case haserl
scripts are like a poor-man's version of PHP (http://www.php.net)

3. It is very small, and so can be used in embedded environments

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall

%files 
%_bindir/*
%_man1dir/*
%_datadir/%name


%changelog
* Sun Nov 06 2005 Nick S. Grechukh <gns@altlinux.org> 0.9.3-alt2
- initial build for sisyphus

