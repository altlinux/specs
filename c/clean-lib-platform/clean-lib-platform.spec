%define srcName clean-platform

Name: clean-lib-platform
Version: 3.44.0
Release: alt1
Summary: Clean platform libraries
Summary(ru_RU.UTF-8): Библиотеки платформы языка Clean (дополнительные к StdEnv)
License: BSD license
Group: Development/Functional
Url: https://clean.cs.ru.nl/
ExclusiveArch: x86_64

Packager: %packager

Source: %srcName-%version.tar
BuildRequires: clean, clean-lib-argenv

%description
This package contains set of libraries, which extend
standard StdEnv library.

%prep
%setup -q -n %srcName-%version

%build

mkdir -p target/clean-lib-platform

mkdir -p target/clean-lib-platform/lib/Platform

# Компиляция C файлов
make -C src/cdeps install

cp -r src/libraries/OS-Independent/* target/clean-lib-platform/lib/Platform/
cp -r src/libraries/OS-Posix/* target/clean-lib-platform/lib/Platform/
cp -r src/libraries/OS-Linux/* target/clean-lib-platform/lib/Platform/
cp -r src/libraries/OS-Linux-64/* target/clean-lib-platform/lib/Platform/
cp -r src/libraries/Platform-x86/* target/clean-lib-platform/lib/Platform/

# Удаляем некомпилирующиеся по разным причинам библиотеки.
rm -rf target/clean-lib-platform/lib/Platform/Text/Parsers/ZParsers/Test
rm -rf target/clean-lib-platform/lib/Platform/Text/GenXML/
rm -rf target/clean-lib-platform/lib/Platform/Clean/
rm -rf target/clean-lib-platform/lib/Platform/Codec/
rm -rf target/clean-lib-platform/lib/Platform/Deprecated/
rm -rf target/clean-lib-platform/lib/Platform/Internet/

rm -rf target/clean-lib-platform/lib/Platform/Data/Dynamic.*
rm -rf target/clean-lib-platform/lib/Platform/Data/Maybe/Gast.*
rm -rf target/clean-lib-platform/lib/Platform/Data/Maybe/GenBinary.*
rm -rf target/clean-lib-platform/lib/Platform/Data/Either/GenPrint.*
rm -rf target/clean-lib-platform/lib/Platform/Data/Set/Gast.*
rm -rf target/clean-lib-platform/lib/Platform/Data/Data.*
rm -rf target/clean-lib-platform/lib/Platform/Data/Encoding/*
rm -rf target/clean-lib-platform/lib/Platform/Data/IntMap*
rm -rf target/clean-lib-platform/lib/Platform/Data/CircularStack*
rm -rf target/clean-lib-platform/lib/Platform/Data/Graph*

rm -f target/clean-lib-platform/lib/Platform/Text/Unicode/Encodings/UTF8/GenHash.*cl
rm -rf target/clean-lib-platform/lib/Platform/Crypto/*
rm -rf target/clean-lib-platform/lib/Platform/Database/*
rm -rf target/clean-lib-platform/lib/Platform/System/AsyncIO*
rm -rf target/clean-lib-platform/lib/Platform/System/_AsyncIO*
rm -rf target/clean-lib-platform/lib/Platform/System/_CopyFile*
rm -rf target/clean-lib-platform/lib/Platform/System/Directory*
rm -rf target/clean-lib-platform/lib/Platform/System/_Directory*
rm -rf target/clean-lib-platform/lib/Platform/System/File*
rm -rf target/clean-lib-platform/lib/Platform/System/_File*
rm -rf target/clean-lib-platform/lib/Platform/System/Process*
rm -rf target/clean-lib-platform/lib/Platform/System/_Process*
rm -rf target/clean-lib-platform/lib/Platform/System/Socket*
rm -rf target/clean-lib-platform/lib/Platform/System/_Socket*
rm -rf target/clean-lib-platform/lib/Platform/System/TTS*
rm -rf target/clean-lib-platform/lib/Platform/System/_TTS*
rm -rf target/clean-lib-platform/lib/Platform/Message/*
rm -rf target/clean-lib-platform/lib/Platform/Network/*
rm -rf target/clean-lib-platform/lib/Platform/Testing/Options*
rm -rf target/clean-lib-platform/lib/Platform/Debug/Performance*

cd target/clean-lib-platform/lib/Platform

# После исправления clm так, чтобы он заранее содержал StdEnv,
# убрать путь к StdEnv!
# Обязательно нужно увеличить кучу cocl, иначе он не может скомпилировать
# модуль Text.HTML
for f in `find . -name "*.icl" | grep -v Gast.icl`; do
  CLEANLIB=/usr/lib64/clean/exe clm -dynamics -aC,-h,100m -I /usr/lib64/clean/StdEnv/ -I . -PO `echo $f | sed s/.icl// | sed s/^..// | sed s:/:.:g`
done

%install

%define libdir %buildroot%_libdir/clean/Platform

mkdir -p %libdir
cp -R target/clean-lib-platform/lib/Platform/* %libdir

%find_lang %name

%post
# Touching compiled files to prevent autogeneration
find /usr/lib64/clean/Platform -name "*.abc" -exec touch {} \;
sleep 1
find /usr/lib64/clean/Platform -name "*.o" -exec touch {} \;

%files
%_libdir/*

%changelog
* Sun Jan 05 2025 Andrey Bergman <vkni@altlinux.org> 3.44.0-alt1
- Update to new version (upstream version is 0.3.44)

* Sun Jan 01 2023 Andrey Bergman <vkni@altlinux.org> 3.19.0-alt1
- Update to new version (upstream version is 0.3.19)

* Tue Oct 25 2022 Andrey Bergman <vkni@altlinux.org> 3.10.0-alt1
- Update to new version (upstream version is 0.3.10)

* Thu Jan 28 2021 Andrey Bergman <vkni@altlinux.org> 3.0.0-alt2
- Update to a new version

* Thu Oct 29 2020 Andrey Bergman <vkni@altlinux.org> 3.0.0-alt1
- Initial release for Sisyphus
