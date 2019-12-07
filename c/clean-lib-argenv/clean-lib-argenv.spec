%define srcName ArgEnvUnix

Name: clean-lib-argenv
Version: 1.0.3
Release: alt2
Summary: Clean low level interface to command line and environment
Summary(ru_RU.UTF-8): Библиотека параметров командной строки для языка Clean
License: BSD license
Group: Development/Functional
Url: https://clean.cs.ru.nl/
ExclusiveArch: x86_64

Packager: %packager

Source: %srcName-%version.tar
BuildRequires: clean

%description
This package contains small library providing access to
command line arguments and environment variables for Clean
programming language.

%prep
%setup -q -n %srcName-%version

%build

# После исправления clm так, чтобы он заранее содержал StdEnv,
# убрать!
CLEANLIB=/usr/lib64/clean/exe/ make CLM="clm -I /usr/lib64/clean/StdEnv/"

%install

%define libdir %buildroot%_libdir/clean/ArgEnv

mkdir -p %libdir
install -pm644 *.icl %libdir
install -pm644 *.dcl %libdir
cp -R "Clean System Files/" %libdir

%find_lang %name

%post
# Touching compiled files to prevent autogeneration
touch "/usr/lib64/clean/ArgEnv/Clean System Files"/*.abc
sleep 1
touch "/usr/lib64/clean/ArgEnv/Clean System Files"/*.o

%files
%_libdir/*

%changelog
* Thu Dec 05 2019 Andrey Bergman <vkni@altlinux.org> 1.0.3-alt2
- Rebuild with new compiler.

* Sat May 04 2019 Andrey Bergman <vkni@altlinux.org> 1.0.3-alt1
- Initial release for Sisyphus.
