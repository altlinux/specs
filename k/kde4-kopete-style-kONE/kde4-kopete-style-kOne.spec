Name: kde4-kopete-style-kONE
Summary: A clean, fast, compact and beauty theme for kopete.
Version: 2.0
Release: alt1
License: GPL
Group: Graphical desktop/KDE
URL: http://kde-look.org/content/show.php/kONE?content=36477
Source: kONE-%version.tar.gz
Source1: kONEwl-%version.tar.gz
BuildArch: noarch
BuildRequires: rpm-macros-kde-common-devel
%define styledir %_K4apps/kopete/styles
%description
A clean, fast, compact and beauty theme for kopete.
Easy to extend trought variants for everybody having minimal CSS knowledge.

This package also includes theme variant by A.Potashev with links
displayed as is (http://kde-look.org/content/show.php/kONEwl?content=133745)

%prep
%setup -c -n %name-%version
%setup -D -T -a 1

%install
%__mkdir_p %buildroot%styledir
cp -pr * %buildroot%styledir

%files
%styledir/*

%changelog
* Wed May 11 2011 Alexey Morozov <morozov@altlinux.org> 2.0-alt1
- Initial build of the official kONE theme and Alexander Potashev's
  variant
