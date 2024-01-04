Name: ttf2cxf_stream
Version: 0.4
Release: alt1

Summary: ttf2cxf_stream converts True Type files to CXF Font file format
License: GPLv2
Group: Engineering

Url: https://www.scorchworks.com/Fengrave/fengrave.html
Source: %name-%version.tar.gz
Packager: Alexei Mezin <alexvm@altlinux.org>
Summary(ru_RU.UTF8): ttf2cxf_stream преобразует шрифты формата True Type в формат CXF

BuildRequires: gcc-c++ libfreetype-devel 



%description
ttf2cxf_stream converts True Type files to CXF Font file format. This program is
used by F-Engrave package.

%description -l ru_RU.UTF8
ttf2cxf_stream преобразует шрифты формата True Type в формат CXF. 
Используется пакетов F-Engrave.

%prep
%setup

%build
%make

%install
install -D -m0755 %name %buildroot/%_bindir/%name

%files
%_bindir/*
 
%changelog
* Thu Jan 04 2024 Alexei Mezin <alexvm@altlinux.org> 0.4-alt1
- Initial build


