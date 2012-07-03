%define ename oof
Name: ansforth-ext-%ename
Version: 0.0
Release: alt3
License: %pubdomain
Group: Development/Other
Summary: Object Oriented extension for ANS Forth systems
Summary(uk_UA.CP1251): Об'єктно-орієнтоване розширення для систем ANS Forth
Summary(ru_RU.CP1251): Объектно-ориентированное расширение для систем ANS Forth
URL: http://www.jwdt.com/~paysan/gforth.html
Source: http://www.jwdt.com/~paysan/%ename.tar
BuildArch: noarch
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses

%description
Object Oriented FORTH (OOF) - extension for ANS Forth systems.

%description -l uk_UA.CP1251
Об'єктно-орієнтоване розширення (OOF) для систем ANS Forth.

%description -l ru_RU.CP1251
Объектно-ориентированное расширение (OOF) для систем ANS Forth.


%prep
%setup -n %ename


%install
install -pD -m 0644 {,%buildroot%prefix/lib/ansforth/}%ename.fs


%files
%doc %{ename}sampl.fs
%dir %prefix/lib/ansforth
%prefix/lib/ansforth/*


%changelog
* Mon Nov 03 2008 Led <led@altlinux.ru> 0.0-alt3
- cleaned up spec

* Mon May 21 2007 Led <led@altlinux.ru> 0.0-alt2
- fixed misprints in Summary and %%description (#11839)
- cleaned up spec
- fixed install lib path

* Tue Feb 07 2006 Led <led@altlinux.ru> 0.0-alt1
- initial build
