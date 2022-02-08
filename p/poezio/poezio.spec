Name: poezio
Version: 0.13.1
Release: alt1

Summary: A console Jabber/XMPP client
Group: Networking/Instant messaging
Url: http://poez.io/en
Source: %name-v%version.tar.gz
License: Zlib
BuildRequires(pre): rpm-build-python3

# Automatically added by buildreq on Wed Mar 06 2019
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libcrypt-devel pkg-config python-base python3 python3-base python3-dev python3-module-OpenSSL python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-docutils python3-module-idna python3-module-imagesize python3-module-jinja2 python3-module-markupsafe python3-module-pkg_resources python3-module-pytz python3-module-requests python3-module-six python3-module-sphinx python3-module-urllib3 sh4 xz
BuildRequires: ctags python3-module-alabaster python3-module-setuptools python3-module-sphinxcontrib-websupport python3-module-sphinx

BuildRequires: python3-devel

Requires: python3-module-%name = %version
Requires: python3-module-%name-themes = %version
Requires: python3-module-%name-plugins = %version

# For more accurate deps:
%python3_req_hier

%description
Poezio is a console Jabber/XMPP client.  Its goal is to use anonymous
connections to simply let the user join MultiUserChats.  This way, the user
doesn't have to create a Jabber account, exactly like people are using
IRC.  Poezio's commands are designed to be (if possible) like commonly
used IRC clients (weechat, irssi, etc).
Since version 0.7, poezio can handle real Jabber accounts along with
roster and one to one conversations, making it a full-featured console
Jabber client, but still MultiUserChats-centered.
In the future, poezio should implement at a 100%% level all XEP related to
MUCs, especially XEP 0045.

%package -n python3-module-%name
Group: Development/Python3
Summary: Supplemental python package for %name, a console Jabber/XMPP client
# Workaround a module name clash between the externally visible namespace and
# the internal one (which we want to allow to use in our subpkgs) --
# we expose the externally visible module by force:
#filter_from_provides /^%(%__python3_deps_internal %name)= [^ ]*$/ d
#py3_provides %name
# Workaround RPM interdep optimization, which gives different results on different
# archs (depending on whether poopt requires %%python3_sitelibdir_noarch):
#py3_requires poopt
%description -n python3-module-%name
Supplemental python package for %name, a console Jabber/XMPP client

%package -n python3-module-%name-plugins
Group: Development/Python3
Summary: Plugins for %name, a console Jabber/XMPP client
%description -n python3-module-%name-plugins
Plugins for %name, a console Jabber/XMPP client

%package -n python3-module-%name-themes
Group: Development/Python3
Summary: Themes for %name, a console Jabber/XMPP client
%description -n python3-module-%name-themes
Themes for %name, a console Jabber/XMPP client

#package -n python3-module-poopt
#Group: Development/Python3
#Summary: Optimized version of some stndard python functions
#description -n python3-module-poopt
#This file is a python3 module for poezio, used to replace some
#time-critical python functions that are too slow

%prep
%setup -n %name-v%version
find * -name \*.py -exec sed -i '1i#!/usr/bin/python3' {} \;
#sed -i 's/sys.path.append(/sys.path.insert(0,/' src/poezio.py

%build
%python3_build
sphinx-build-3 %_smp_mflags -b html -d build/doctrees doc/source build/html

%install
%python3_install

%files
%doc build/html
%exclude %_defaultdocdir/%name/source
%_man1dir/*
%_bindir/*
%_datadir/%name
%_desktopdir/*
%_datadir/metainfo/*

#files -n python3-module-poopt
#python3_sitelibdir/poopt.*.so

%files -n python3-module-%name
%python3_sitelibdir/%name
%python3_sitelibdir/%name-*

%files -n python3-module-%name-plugins
%python3_sitelibdir/%{name}_plugins

%files -n python3-module-%name-themes
%python3_sitelibdir/%{name}_themes

%changelog
* Tue Feb 08 2022 Fr. Br. George <george@altlinux.ru> 0.13.1-alt1
- Autobuild version bump to 0.13.1

* Wed Mar 06 2019 Fr. Br. George <george@altlinux.ru> 0.12-alt1
- Autobuild version bump to 0.12

* Mon Aug 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9-alt5
- NMU: updated build dependencies.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9-alt4.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Jul 22 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt4
- (.spec) minor cleanup (of a workaround).

* Fri Jul 22 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt3
- (.spec) %%python3_req_hier for more accurate deps.

* Thu Jul 21 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt2
- (.spec) declare that our modules set up a non-std path for imports
  (when they are loaded) with %%allow_python3_import_path.
- (.spec) poopt subpkg shouldn't include other files.

* Wed Jul 20 2016 Fr. Br. George <george@altlinux.ru> 0.9-alt1
- Autobuild version bump to 0.9
- Separate modules

* Tue Mar 25 2014 Fr. Br. George <george@altlinux.ru> 0.8.1-alt1
- Autobuild version bump to 0.8.1

* Thu Mar 13 2014 Fr. Br. George <george@altlinux.ru> 0.8-alt1
- Autobuild version bump to 0.8

