Name: RHVoice
Version: 0.5
Release: alt1

Summary: RHVoice is a Russian speech synthesizer written by Olga Yakovleva

Packager: Michael Pozhidaev <msp@altlinux.org>

License: %gpl3plus
Group: Sound
Url: https://github.com/Olga-Yakovleva/RHVoice

BuildPreReq: rpm-macros-tts

# manually removed: cmdtest cvs dblatex distcc-pump dmd dreampie fail2ban flex genbackupdata ghostscript-utils gitum gyp meld mercurial mydbf2mysql patool python-module-9ML python-module-BeautifulSoup python-module-ClientForm
# Automatically added by buildreq on Sun Apr 24 2016
# optimized out: bzr ghostscript-classic glib2-devel ipython libgio-devel libgpg-error libjson-c libsigc++2-devel libstdc++-devel pkg-config policycoreutils python-base python-devel python-module-4Suite-XML python-module-BTrees python-module-Fabric python-module-FormEncode python-module-GitDB python-module-GitPython python-module-IPy python-module-MySQLdb python-module-OpenGL python-module-OpenGL_accelerate python-module-OpenSSL python-module-Pillow python-module-PyStemmer python-module-Pygments python-module-Reportlab python-module-SQLAlchemy python-module-SQLObject python-module-ZODB python-module-acme python-module-apsw python-module-babel python-module-backports.ssl_match_hostname python-module-beaker python-module-boto python-module-certifi python-module-cffi python-module-chameleon.core python-module-chardet python-module-cheetah python-module-cherrypy2 python-module-cliapp python-module-cliff python-module-cmd2 python-module-configargparse python-module-configobj python-module-coverage python-module-cryptography python-module-cssselect python-module-cups python-module-cycler python-module-dateutil python-module-debtcollector python-module-decorator python-module-dexml python-module-dialog python-module-distribute python-module-django python-module-django-appconf python-module-dns python-module-docutils python-module-ecdsa python-module-ed25519 python-module-elementtree python-module-enum34 python-module-extras python-module-fixtures python-module-flup python-module-fs python-module-funcsigs python-module-functools32 python-module-fuse python-module-future python-module-futures python-module-gdata python-module-genshi python-module-gevent python-module-geventutil python-module-gflags python-module-google python-module-google-apputils python-module-greenlet python-module-httplib2 python-module-idna python-module-ipaddress python-module-ipykernel python-module-ipython_genutils python-module-iso8601 python-module-itsdangerous python-module-jinja2 python-module-jsonpatch python-module-jsonpointer python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-keyczar python-module-keystoneclient python-module-libarchive python-module-linecache2 python-module-lingua python-module-lxml python-module-m2crypto python-module-markdown python-module-markupsafe python-module-matplotlib python-module-mimeparse python-module-mistune python-module-mock python-module-monotonic python-module-mpmath python-module-msgpack python-module-mwclient python-module-nbconvert python-module-nbformat python-module-ndg python-module-ndg-httpsclient python-module-netaddr python-module-netifaces python-module-nose python-module-notebook python-module-nss python-module-ntlm python-module-numpy python-module-odfpy python-module-openid python-module-oslo.config python-module-oslo.i18n python-module-oslo.policy python-module-oslo.serialization python-module-oslo.utils python-module-paramiko python-module-parsedatetime python-module-paste python-module-path python-module-pbr python-module-peak python-module-persistent python-module-pexpect python-module-pickleshare python-module-pluggy python-module-ply python-module-polib python-module-prettytable python-module-protocols python-module-psutil python-module-psycopg2 python-module-ptyprocess python-module-py python-module-pyasn1 python-module-pyasn1-modules python-module-pycares python-module-pycparser python-module-pycrypto python-module-pycryptopp python-module-pycurl python-module-pyftpdlib python-module-pyglet python-module-pygobject3 python-module-pyinotify python-module-pymongo python-module-pyparsing python-module-pypdf python-module-pyrfc3339 python-module-pytest python-module-pytz python-module-qserve python-module-requests python-module-roman python-module-scapy python-module-scipy python-module-serial python-module-simplegeneric python-module-simplejson python-module-six python-module-slip python-module-smmap python-module-snappy python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-stevedore python-module-sympy python-module-tempita python-module-terminado python-module-testtools python-module-timelib python-module-tinyec python-module-tornado python-module-tornado_xstatic python-module-traceback2 python-module-tracing python-module-traitlets python-module-transaction python-module-trollius python-module-ttystatus python-module-twisted-core python-module-unicodecsv python-module-unittest2 python-module-urllib3 python-module-versiontools python-module-warlock python-module-webob python-module-werkzeug python-module-whoosh python-module-wrapt python-module-wx2.9 python-module-xlwt python-module-xstatic python-module-xstatic-term.js python-module-yaml python-module-ydbf python-module-z3c python-module-z3c.recipe python-module-zc python-module-zc.buildout python-module-zc.lockfile python-module-zc.recipe python-module-zc.recipe.egg python-module-zc.zlibstorage python-module-zconfig python-module-zdaemon python-module-zmq python-module-zodbpickle python-module-zope python-module-zope.event python-module-zope.hookable python-module-zope.interface python-module-zope.proxy python-modules python-modules-compiler python-modules-wsgiref python3 python3-base ruby ruby-stdlibs texlive-base-bin texlive-latex-base
BuildRequires: gcc-c++ libao-devel libglibmm-devel libportaudio2-devel libpulseaudio-devel scons

BuildRequires: flite-devel libunistring-devel scons
BuildRequires: rpm-build-licenses

Requires: tts-base

# Source-url: https://github.com/Olga-Yakovleva/RHVoice/archive/%version.tar.gz
Source: RHVoice-%version.tar
Source2: rhvoice.voiceman
Source3: rhvoice-en.voiceman

%description
RHVoice is a Russian speech synthesizer written by Olga Yakovleva.
It uses the following free software components:
* Russian speech database and Russian language description for
  Festival by Nickolay V. Shmyrev (https://developer.berlios.de/projects/festlang)
  The phoneset and almost all of the main lts rules are used as is,
  but I've made changes in other parts, either to simplify conversion
  to the flite format, or to add new features, or just to understand
  how it all works.
* The voice has been trained with The HMM-based Speech Synthesis
  System (HTS) (http://hts.sp.nitech.ac.jp)
* The hts_engine API is used for runtime speech generation
  (http://hts-engine.sourceforge.net/)
  Since the library does not support streaming synthesis, the original
  version has been modified to implement this functionality, and the
  synthesizer distribution includes this patched version.
* The C implementation of the Russian text analyzer uses Flite
  (http://www.speech.cs.cmu.edu/flite)
  I used the flite's implementation of English language support as an
  example, some functions were used as a starting point.
* the stress information for the stress dictionary has been extracted
  from the test dictionary in the RuLex package by Igor B. Poretsky
  (http://poretsky.homelinux.net/packages/)
* GNU libunistring is used for working with unicode text
  (http://www.gnu.org/software/libunistring/)

%package -n lib%name
Summary: RHVoice is a Russian speech synthesizer written by Olga Yakovleva
Group: System/Libraries
Requires: %name = %version-%release

%description -n lib%name
RHVoice is a Russian speech synthesizer written by Olga Yakovleva.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development files for %name

%prep
%setup

%build
%add_optflags -std=c++11
scons CXXFLAGS="%optflags" prefix=%_prefix libdir=%_libdir sysconfdir=%_sysconfdir

%install
#make DESTDIR=%buildroot install
scons install DESTDIR=%buildroot prefix=%_prefix libdir=%_libdir sysconfdir=%_sysconfdir
%__install -pD -m 644 %SOURCE2 %buildroot%_ttsdir/rhvoice.voiceman
%__install -pD -m 644 %SOURCE3 %buildroot%_ttsdir/rhvoice-en.voiceman

%preun
%tts_unregister rhvoice
%tts_unregister rhvoice-en

%files
%doc COPYING NEWS README
%dir %_sysconfdir/RHVoice/
%config(noreplace) %_sysconfdir/RHVoice/RHVoice.conf
%_ttsdir/*
%_bindir/*
%_datadir/%name/
%_datadir/dbus-1/services/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/RHVoice.h
%_includedir/RHVoice_common.h

%changelog
* Sun Apr 24 2016 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- build 0.5 from https://github.com/Olga-Yakovleva/RHVoice

* Thu Apr 07 2011 Michael Pozhidaev <msp@altlinux.ru> 0.3-alt3
- Added VoiceMan configuration for English in translit mode

* Tue Apr 05 2011 Michael Pozhidaev <msp@altlinux.ru> 0.3-alt2
- Added tts_unregister call to preun section
- tts-devel buildreq replaced by rpm-macros-tts

* Mon Jan 31 2011 Michael Pozhidaev <msp@altlinux.ru> 0.3-alt1
- New version with fixed flite sprintf bug and autotools support

* Wed Jul 28 2010 Michael Pozhidaev <msp@altlinux.ru> 0.1-alt1
- First release for ALT Linux Sisyphus

