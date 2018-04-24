Name: altlinux-repolist-utils
Version: 0.002
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: map src/bin names and files in ALTLinux repos using src.list/bin.list
Group: Development/Other
License: GPL or Artistic
Source: %name-%version.tar
#Url: http://www.altlinux.org/

BuildRequires: rpm-build-perl perl(Source/Shared/FindLocalMirror/ALTLinux.pm)

%description
%summary

%prep
%setup

%build

%install
mkdir -p %buildroot%_bindir
install -m 755 altlinux-repolist-*-to-* %buildroot%_bindir/
mkdir -p %buildroot%perl_vendor_privlib/ALTLinux/
install -m 644 *.pm %buildroot%perl_vendor_privlib/ALTLinux/

%files
%doc README
%_bindir/*
%perl_vendor_privlib/ALTLinux/*.pm

%changelog
* Tue Apr 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- new version

* Sat Apr 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- new version
