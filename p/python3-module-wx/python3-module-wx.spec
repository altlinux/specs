# for now, sphinx fails on armh :( remove when fixed.
%def_enable archdocs
%ifarch armh
# for now, sphinx fails on armh :(
%def_disable docs
%else
%def_enable docs
%endif
Name:		python3-module-wx
Version:	4.0.7
Release:	alt6.2
Group:		Development/Python3
Summary:	The cross-platform GUI toolkit for the Python language
URL:		https://pypi.org/project/wxPython
License:	GPL-2.0+ WITH WxWindows-exception-3.1
Source:		wxPython-%version.tar.gz
Patch:		wxPython-4.0.7-alt-fixes.patch
Patch1:		wxPython-4.0.7-alt-demofix.patch

# Automatically added by buildreq on Sun Mar 29 2020
# optimized out: at-spi2-atk fontconfig glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcrypt-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libglvnd-devel libgpg-error libgst-plugins1.0 libharfbuzz-devel libharfbuzz-icu libpango-devel libstdc++-devel libwayland-client libwayland-cursor libwayland-egl libwayland-server libwpebackend-fdo libwxBase3.0-devel libwxGTK3.0-gl libwxGTK3.0-media libwxGTK3.0-webview pkg-config python2-base python3 python3-base python3-module-OpenSSL python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-docutils python3-module-html5lib python3-module-idna python3-module-imagesize python3-module-jinja2 python3-module-lxml python3-module-markupsafe python3-module-packaging python3-module-pkg_resources python3-module-pytz python3-module-requests python3-module-six python3-module-sphinx python3-module-urllib3 python3-module-webencodings sh4 termutils xorg-proto-devel xz
BuildRequires: gcc-c++ libgtk+3-devel libwxGTK3.0-devel python3-dev python3-module-BeautifulSoup4 git-core libglvnd-devel
%if_enabled docs
BuildRequires: python3-module-sphinx
%endif

# pip is used in wget as latest fallback, but we have wget or urllib
%add_python3_req_skip pip

%description
wxPython is a cross-platform GUI toolkit for the Python programming
language. It allows Python programmers to create programs with a robust,
highly functional graphical user interface, simply and easily. It is
implemented as a set of Python extension modules that wrap the GUI
components of the popular wxWidgets cross platform library, which is
written in C++.

Like Python and wxWidgets, wxPython is Open Source, which means that it
is free for anyone to use and the source code is available for anyone to
look at and modify. And anyone can contribute fixes or enhancements to
the project.

%package demo
Summary: Demo programs for wxPython
Group: Development/Python3
License:	GPL-2.0+ WITH WxWindows-exception-3.1
%description demo
%summary

%add_python3_self_prov_path %buildroot%python3_sitelibdir/wx/demo

%package utils
Summary: Development tools for wxPython
Group: Development/Python3
License:	GPL-2.0+ WITH WxWindows-exception-3.1
Provides:	pycrust = %version-%release
Conflicts: python-module-wx3.0
%description utils
%summary

%package docs
Summary: Documentation for wxPython
%if_disabled archdocs
BuildArch: noarch
%endif
Group: Development/Python3
License:	GPL-2.0+ WITH WxWindows-exception-3.1
%description docs
%summary

%prep
%setup -n wxPython-%version
%patch -p1
%patch1 -p1
sed -i 's/sphinx-build /sphinx-build-3 -j'${NPROCS:-%__nprocs}' /' build.py

# Hack out python2
for F in `grep -rl '#!/usr/bin/env python$' [^b]*/*`; do
	sed -i 's@#!/usr/bin/env python$@#!/usr/bin/python3@' "$F"
done

# Hack off NoUri migration
sed -i 's/from sphinx.environment import NoUri/from sphinx.errors import NoUri/' docs/sphinx/availability.py
# Hack off sphinx 4.0.x api change
sed -i 's/add_javascript/add_js_file/g' docs/sphinx/availability.py


git init
git config user.email "%packagerAddress"
git config user.name "%packagerName"
git add b
git commit -a -m "%name-%version-%release"
git tag "%name-%version-%release"

%build
python3 build.py build_py \
%if_enabled docs
    sphinx \
%endif
    --prefix="%_prefix" --python=`which python3` --debug --use_syswx

%install
%python3_install
mkdir -p %buildroot%_datadir
mv %buildroot%python3_sitelibdir/wx/locale %buildroot%_datadir
mkdir -p %buildroot%python3_sitelibdir_noarch
cp -a demo %buildroot%python3_sitelibdir/wx/demo
# TODO icon/desktop for pycrust/demo

%find_lang wxstd

%add_python3_req_skip wx.activex comtypes.client comtypes.gen comtypes.hresult comtypes win32com.client.gencache __main__

%files -f wxstd.lang
%doc [A-Z]*.*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/wx/demo

%if_enabled docs
%files docs
%doc docs/html samples
%endif

%files demo
%python3_sitelibdir/wx/demo

%files utils
%doc wx/py/README.txt
%_bindir/*

%changelog
* Thu Dec 29 2022 Valery Inozemtsev <shrek@altlinux.ru> 4.0.7-alt6.2
- updated build dependencies

* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 4.0.7-alt6.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Mon Oct 11 2021 Igor Vlasenko <viy@altlinux.org> 4.0.7-alt6
- NMU: disabled docs on armh (fix rebuild)

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 4.0.7-alt5
- NMU: disable pip require, drop BR: ctags

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 4.0.7-alt4
- add Conflicts with python-module-wx3.0 (ALT bug 38541)

* Tue May 25 2021 Fr. Br. George <george@altlinux.ru> 4.0.7-alt3
- Build with new sphinx

* Tue Apr 27 2021 Fr. Br. George <george@altlinux.ru> 4.0.7-alt2
- Build with new sphinx

* Mon Mar 30 2020 Fr. Br. George <george@altlinux.ru> 4.0.7-alt1
- Initial wxPython Phoenix project build for ALT

