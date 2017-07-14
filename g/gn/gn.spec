%def_with bootstrap

Name: gn
Version: 0.0.0
Release: alt1

Summary: GN is a meta-build system that generates NinjaBuild files

License: BSD-style
Group: Development/C++
Url: https://chromium.googlesource.com/chromium/src/tools/gn/

# Source-git: https://chromium.googlesource.com/chromium/src/tools/gn/
Source: %name-%version.tar

# Automatically added by buildreq on Sat Jul 29 2017
# optimized out: glibc-kernheaders-x86 libstdc++-devel python-base python-modules python-modules-compiler python-modules-logging python-modules-unittest python3 python3-base
BuildRequires: gcc-c++ libevent-devel libgtest-devel ninja-build

%if_with bootstrap
BuildRequires: python-modules python-modules-logging
%else
BuildRequires: gn
%endif

%description
GN is a meta-build system that generates NinjaBuild files so that you can build Chromium with Ninja.

GN is a GYP replacement
GN files are more readable and more maintainable than GYP files.
GN is 20x faster than GYP.

%prep
%setup
mv tools/gn/.gear/build .
mv tools/gn/.gear/base .

# use external libgtest
find -name "*.cc" | xargs subst "s|testing/gtest/include|%_includedir|g"
find -name "*.h" | xargs subst "s|testing/gtest/include|%_includedir|g"
# use external libevent
find -name "*.cc" | xargs subst "s|base/third_party/libevent|%_includedir|g"

%if_with bootstrap
cd tools/gn
%__subst "s|'ninja'|'ninja-build'|g" bootstrap/bootstrap.py
#__subst "s|SRC_ROOT =.*|SRC_ROOT = '$(pwd)'|g" bootstrap/bootstrap.py
#__subst "s|tools/gn/gn_main.cc|gn_main.cc|g" bootstrap/bootstrap.py

# use external libevent
%__subst "s|'-latomic'|'-latomic', '-levent'|g" bootstrap/bootstrap.py
%__subst "20idisable_static_libraries = {}" bootstrap/bootstrap.py
%__subst "s|static_libraries\['libevent'\]|disable_static_libraries['libevent']|g" bootstrap/bootstrap.py

%endif

%build
cd tools/gn
%if_with bootstrap
./bootstrap/bootstrap.py -v --no-rebuild --debug
%else
gn --root=$(pwd) --dotfile=BUILD.gn gen out
%endif

%install
install -m755 -D out/Debug/gn %buildroot%_bindir/gn

%files
%_bindir/%name

%changelog
* Fri Jul 14 2017 Vitaly Lipatov <lav@altlinux.ru> 0.0.0-alt1
- initial build for ALT Sisyphus
