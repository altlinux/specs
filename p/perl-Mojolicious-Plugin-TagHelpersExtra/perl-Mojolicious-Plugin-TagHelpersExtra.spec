%def_without test

Name: perl-Mojolicious-Plugin-TagHelpersExtra
Version: 0.1
Release: alt1
Summary: Extra HTML tag plugins for Mojolicious Perl Web Framework, including link_to_here and table.

Group: Development/Perl
License: Perl
Url: http://github.com/kvorg/mojolicious-plugin-tag_helpers_extra

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-Mojolicious

%description
%name

%prep
%setup -q

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Mojolicious/Plugin/*.pm
%doc README.pod

%changelog
* Mon Mar 05 2012 Eugene Prokopiev <enp@altlinux.ru> 0.1-alt1
- initial build

