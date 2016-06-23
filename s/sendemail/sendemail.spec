Name: sendemail
Version: 1.56
Release: alt1

Summary: Send email from a console near you!
License: GPLv2+
Group: Networking/Mail

URL: https://github.com/mogaal/sendemail
Source: %name-%version.tar

BuildArch: noarch

%description
SendEmail is a lightweight, completly command line based,
SMTP email agent. If you have the need to send email from
the command line, this tool is perfect. It was designed to be used
in bash scripts, Perl programs, and web sites, but it is also quite
useful in many other contexts.  SendEmail is written in Perl
and is unique in that it requires NO SPECIAL MODULES.
It has an intuitive and flexible set of command-line options,
making it very easy to learn and use.

%prep
%setup

%build

%install
mkdir -pv %buildroot/%_bindir
cp -v sendEmail sendEmail.pl %buildroot/%_bindir/

%files
%doc CHANGELOG README README-BR.txt TODO
%_bindir/sendEmail*

%changelog
* Thu Jun 23 2016 Lenar Shakirov <snejok@altlinux.ru> 1.56-alt1
- First build for Sisyphus

