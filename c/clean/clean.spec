%define srcName clean

Name: clean
Version: 3.0
Release: alt1.1
Summary: The Clean programming language compiler and environment
Summary(ru_RU.UTF-8): Компилятор и системная библиотека для языка Clean
License: BSD license
Group: Development/Functional
Url: https://clean.cs.ru.nl/
ExclusiveArch: x86_64

# Пакет базируется на сборочных скриптах компилятора, как рекомендовано
# разработчиками Clean (Джоном и Камилом).
#
# Сборочные скрипты можно скачать в
#    https://gitlab.science.ru.nl/clean-and-itasks/clean-build
#
# Исходные каталоги:
#  clean/build - тут лежит bootstrap compiler
#  clean/clean-base - часть сборочных скриптов
#  clean/src - деревья исходных кодов компилятора и базовых библиотек


Packager: %packager

Source: clean-%version.tar

%description
This package contains a Clean language compiler and standard
library. This is a bootstrap package for 64-bit intel architecture.

%prep
%setup -q -n %srcName-%version

%build

./clean-base/linux-x64/build.sh clean-base linux x64

# Компилируем стандартную библиотеку - надо спросить Камила
cd target/clean-base/lib/StdEnv/
for f in `ls *.icl`; do
  PATH=$PATH:../../bin/ CLEANLIB=../exe clm -I . -PO `echo $f | sed s/.icl//`
done
PATH=$PATH:../../bin/ CLEANLIB=../exe clm -I . -PO StdEnv
cd ../../../../

%install
%define docdir %_docdir/%name-%version
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_libdir/%name
mkdir -p %buildroot%docdir
mkdir -p %buildroot%_mandir

%define target target/clean-base/

install -pm755 %target/bin/* %buildroot/%_bindir/
cp -R %target/lib/* %buildroot%_libdir/%name
cp -R %target/doc %buildroot%docdir

# Это костыль, его нужно убрать - я отправил письмо Камиллу,
# что man страница не устанавливается в target.
install -pm644 src/clm-master/clm.1 %buildroot%_mandir

%find_lang %name

%post
# Touching compiled files to prevent autogeneration
touch "/usr/lib64/clean/StdEnv/Clean System Files"/*.abc
sleep 1
touch "/usr/lib64/clean/StdEnv/Clean System Files"/*.o

%files
%_bindir/*
%_libdir/*
%_mandir/*
%%dir %docdir
%docdir/*

%changelog
* Fri May 03 2019 Andrey Bergman <vkni@altlinux.org> 3.0-alt1.1
- Add exclusive arch

* Thu May 02 2019 Andrey Bergman <vkni@altlinux.org> 3.0-alt1
- Initial release for Sisyphus.

