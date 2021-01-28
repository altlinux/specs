%define srcName gast

Name: clean-lib-gast
Version: 1.0.0
Release: alt3
Summary: GAST: A Generic Automatic Software Test-system for Clean
Summary(ru_RU.UTF-8): Библиотека автоматического тестирования для языка Clean
License: BSD license
Group: Development/Functional
Url: https://clean.cs.ru.nl/
ExclusiveArch: x86_64

Packager: %packager

Source: %srcName-%version.tar
BuildRequires: clean, clean-lib-platform

%description
GAST: A Generic Automatic Software Test-system.

%prep
%setup -q -n %srcName-%version

%build

cd Libraries
CLEANLIB=/usr/lib64/clean/exe/ clm -PO -I /usr/lib64/clean/Platform/ Gast

%install

%define libdir %buildroot%_libdir/clean/Gast

mkdir -p %libdir
install -pm644 Libraries/Gast.icl %libdir
install -pm644 Libraries/Gast.dcl %libdir
cp -R Libraries/"Clean System Files/" %libdir

mkdir -p %libdir/Gast
install -pm644 Libraries/Gast/*.icl %libdir/Gast/
install -pm644 Libraries/Gast/*.dcl %libdir/Gast/
cp -R Libraries/Gast/"Clean System Files/" %libdir/Gast/

%find_lang %name

%post
# Touching compiled files to prevent autogeneration
find /usr/lib64/clean/Gast -name "*.abc" -exec touch {} \;
sleep 1
find /usr/lib64/clean/Gast -name "*.o" -exec touch {} \;

%files
%_libdir/*

%changelog
* Thu Jan 28 2021 Andrey Bergman <vkni@altlinux.org> 1.0.0-alt3
- Update Gast to a new version.

* Fri Oct 30 2020 Andrey Bergman <vkni@altlinux.org> 1.0.0-alt2
- Correct location of internal files.

* Thu Oct 29 2020 Andrey Bergman <vkni@altlinux.org> 1.0.0-alt1
- Initial release for Sisyphus.
