Name: appliance-mithraen-recoll
Summary: Virtual package that requires some recoll filters
Version: 0.0.1
Release: alt1
License: GPL
Group: System/Base

Url: http://git.altlinux.org/people/mithraen/packages/appliance-mithraen-recoll.git

BuildArch: noarch

Packager: Denis Smirnov <mithraen@altlinux.ru>

Requires: recoll
Requires: perl-Image-ExifTool
Requires: antiword
Requires: python-module-pychm
Requires: aspell aspell-ru-rk

%description
%summary

%prep
%build
%install
mkdir -p %buildroot

%files
%changelog
* Sat Oct 16 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- first build for Sisyphus
