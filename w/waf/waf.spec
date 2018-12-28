%def_with python3
%add_python3_path %_datadir/waf3
Name: waf
Version: 2.0.14
Release: alt1

Summary: A Python-based build system
License: BSD
Group: Development/Other

URL: http://code.google.com/p/waf/
# git https://github.com/waf-project/waf
Source: %name-%version.tar
Patch0: waf-1.6.2-libdir.patch
Patch1: waf-1.6.9-logo.patch
# with python-3 waf does not find the top_dir directory with wscript and this path try to fix it
Patch2: waf-2.0.12-python3-build.patch

# Automatically added by buildreq on Mon Aug 09 2010
BuildRequires: python-devel python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging

BuildArch: noarch

%if_with python3
BuildRequires: python3-devel 
BuildRequires(pre): rpm-build-python3
%endif

%description
Waf is a Python-based framework for configuring, compiling and installing
applications. It is a replacement for other tools such as Autotools, Scons,
CMake or Ant.

%if_with python3
%package -n python3-module-waf
Group: Development/Tools
Summary:        Python3 support for %{name}

%description -n python3-module-waf
Waf is a Python-based framework for configuring, compiling and
installing applications. It is a replacement for other tools such as
Autotools, Scons, CMake or Ant.

This package contains the Python 3 version of %{name}.
%endif # with_python3

%prep
%setup
# also search for waflib in /usr/share/waf
%patch0 -p0
# do not try to use the (removed) waf logos
%patch1 -p1
%patch2 -p1

# remove BOM, causes trouble later
sed -i -e '1s/^\xEF\xBB\xBF//' waflib/extras/dpapi.py

# add missing quotes, see rhbz#914566 and
# https://code.google.com/p/waf/issues/detail?id=1263
sed -i -e 's@fontname=\(Vera.*sans\),@fontname="\1",@g' \
  docs/sphinx/conf.py \
  docs/sphinx/coremodules.rst \
  docs/sphinx/featuremap.rst

%build
./configure --prefix=/usr
# skip build slow_qt4 extras
rm -f waflib/extras/slow_qt4.py
extras=
for f in waflib/extras/*.py ; do
  f=$(basename "$f" .py);
  if [ "$f" != "__init__" ]; then
    extras="${extras:+$extras,}$f" ;
  fi
done
./waf-light --make-waf --strip --tools="$extras"

%install
#./waf install --yes --destdir=%buildroot

# use waf so it unpacks itself
mkdir _temp ; pushd _temp
cp -av ../waf .
%{__python} ./waf >/dev/null 2>&1
pushd .waf-%{version}-*
find . -name '*.py' -printf '%%P\0' |
  xargs -0 -I{} install -m 0644 -p -D {} %{buildroot}%{_datadir}/waf/{}
popd
%if_with python3
%{__python3} ./waf >/dev/null 2>&1
pushd .waf3-%{version}-*
find . -name '*.py' -printf '%%P\0' |
  xargs -0 -I{} install -m 0644 -p -D {} %{buildroot}%{_datadir}/waf3/{}
popd
%endif # with_python3
popd

# install the frontend
install -m 0755 -p -D waf-light %{buildroot}%{_bindir}/waf-%{__python_version}
%if_with python3
install -m 0755 -p -D waf-light %{buildroot}%{_bindir}/waf-%{__python3_version}
%endif # with_python3
ln -s waf-%{__python_version} %{buildroot}%{_bindir}/waf

# remove shebangs from and fix EOL for all scripts in wafadmin
find %{buildroot}%{_datadir}/ -name '*.py' \
     -exec sed -i -e '1{/^#!/d}' -e 's|\r$||g' {} \;

# fix waf script shebang line
sed -i "1c#! %{__python}" %{buildroot}%{_bindir}/waf-%{__python_version}
%if_with python3
sed -i "1c#! /usr/bin/python3" %{buildroot}%{_bindir}/waf-%{__python3_version}
%endif # with_python3

# remove x-bits from everything going to doc
find demos utils -type f -exec chmod 0644 {} \;

# remove hidden file
rm -f docs/sphinx/build/html/.buildinfo

%files
%_bindir/waf
%_bindir/waf-2.7
%_datadir/waf

%if_with python3
%files -n python3-module-waf
%{_bindir}/waf-%__python3_version
%{_datadir}/waf3
%endif # with_python3


%changelog
* Fri Dec 28 2018 Anton Farygin <rider@altlinux.ru> 2.0.14-alt1
- 2.0.14

* Wed Dec 12 2018 Anton Farygin <rider@altlinux.ru> 2.0.13-alt1
- 2.0.13

* Tue Oct 09 2018 Anton Farygin <rider@altlinux.ru> 2.0.12-alt1
- 2.0.12

* Wed May 30 2018 Anton Farygin <rider@altlinux.ru> 2.0.8-alt1
- new version

* Tue Apr 03 2018 Anton Farygin <rider@altlinux.ru> 1.9.15-alt1
- new version

* Tue Sep 19 2017 Anton Farygin <rider@altlinux.ru> 1.9.14-alt1
- new version
- fixed shebang for waf-3.5

* Sun Jun 04 2017 Anton Farygin <rider@altlinux.ru> 1.9.12-alt1
- updated to 1.9.12

* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.10-alt2
- python3 support

* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.10-alt1
- 1.7.10 (closes: 28285)
- TODO: python3

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.18-alt2.1
- Rebuild with Python-2.7

* Sun Jul 17 2011 Victor Forsiuk <force@altlinux.org> 1.5.18-alt2
- Build with enabled req-finder (closes: #25802).

* Mon Aug 09 2010 Victor Forsiuk <force@altlinux.org> 1.5.18-alt1
- 1.5.18

* Wed Jun 16 2010 Victor Forsiuk <force@altlinux.org> 1.5.17-alt1
- 1.5.17

* Tue Mar 30 2010 Victor Forsiuk <force@altlinux.org> 1.5.15-alt1
- 1.5.15

* Fri Feb 19 2010 Victor Forsiuk <force@altlinux.org> 1.5.13-alt1
- 1.5.13

* Mon Feb 15 2010 Victor Forsiuk <force@altlinux.org> 1.5.12-alt1
- 1.5.12

* Sat Jan 30 2010 Victor Forsyuk <force@altlinux.org> 1.5.11-alt1
- Initial build.
