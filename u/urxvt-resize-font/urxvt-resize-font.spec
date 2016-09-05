%define	_urxvt_perl_dir %_libdir/urxvt/perl

Name:		urxvt-resize-font
Version:	2016.04.27.0
Release:	alt1

Source0:	%name-%version.tar.gz
Source1:	README.ALT-ru_RU.UTF-8

Summary:	An urxvt plugin to adjust the font size on the fly
License:	MIT
Group:		Other
Requires:	rxvt-unicode

%description
%summary.

%prep
%setup
cp -- %SOURCE1 .

%install
mkdir -p %buildroot%_urxvt_perl_dir
install -pm 644 resize-font -t %buildroot%_urxvt_perl_dir

%files
%doc README.ALT-ru_RU.UTF-8
%_urxvt_perl_dir/resize-font

%changelog
* Fri Sep 02 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 2016.04.27.0-alt1
- Initial build.

