# TODO
%def_with plugins

Name: certbot
Version: 0.21.0
Release: alt1

Summary: A free, automated certificate authority client

License: ASL 2.0
Group: Networking/Other
Url: https://certbot.eff.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# #Source-url: https://pypi.python.org/packages/source/l/%name/%name-%version.tar.gz
# Source-url: https://github.com/certbot/certbot/archive/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-devel python-module-distribute

#Requires: python-module-%name = %version-%release
Provides: python-module-%name = %EVR
Obsoletes: python-module-%name < %EVR

Requires: python-module-zope.component
Requires: python-module-zope.interface >= 4.1.0
Requires: python-module-pyasn1 >= 0.1.8
Requires: python-module-cffi >= 1.4.2
Requires: python-module-setuptools >= 13
# Due Prior to Python 2.7.9 the stdlib SSL module did not allow a user to configure
# See /usr/lib/python2.7/site-packages/acme/client.py
Requires: python-base >= 2.7.9

# Required for documentation
#BuildRequires: python-sphinx
#BuildRequires: python-sphinx_rtd_theme
#BuildRequires: python-repoze-sphinx-autointerface
#BuildRequires: python-sphinxcontrib-programoutput

BuildRequires: python-module-acme >= %version

Provides: letsencrypt = %version
Obsoletes: letsencrypt

%define certbotdir %_datadir/%name
%add_python_req_skip certbot

%description
Let's Encrypt is a free, automated certificate authority that aims
to lower the barriers to entry for encrypting all HTTP traffic on the internet.

# TODO: move to /usr/share/%name
%package -n python-module-%name
Group: Networking/Other
Requires: python-module-configargparse >= 0.10.0
# already in core python
#Requires: python-module-argparse
Requires: python-module-psutil >= 2.1.0
Requires: python-module-acme >= %version
#Recommends: letsencrypt-doc
Summary: Python 2 libraries used by %name

Provides: python-module-letsencrypt = %version
Obsoletes: python-module-letsencrypt


%description -n python-module-%name
The python2 libraries to interface with letsencrypt.

# TODO
%if_with plugins
%package apache
Group: Networking/Other
Summary: Certbot Apache plugin
AutoProv: no
Requires: %name = %version-%release

%description apache
Certbot Apache plugin.

%package nginx
Group: Networking/Other
Summary: Certbot nginx plugin
AutoProv: no
Requires: %name = %version-%release

%description nginx
Certbot nginx plugin.
%endif

%prep
%setup

%build
%python_build

cd certbot-apache
%python_build
cd ../certbot-nginx
%python_build


%install
%python_install --install-purelib=%certbotdir

cd certbot-apache
%python_install --install-purelib=%certbotdir
cd ../certbot-nginx
%python_install --install-purelib=%certbotdir
cd -

# TODO: remove compat dirs
mkdir -p %buildroot%_sysconfdir/letsencrypt
ln -s letsencrypt %buildroot%_sysconfdir/%name
mkdir -p %buildroot%_sharedstatedir/letsencrypt
ln -s letsencrypt %buildroot%_sharedstatedir/%name
mkdir -p %buildroot%_logdir/letsencrypt
ln -s letsencrypt %buildroot%_logdir/%name

ln -s %name %buildroot%_bindir/letsencrypt

#  it is better do not require argparse on python >= 2.7.
#__subst "s|^argparse$||" %buildroot%python_sitelibdir/%name-%{version}*.egg-info/requires.txt

%__subst 's|^__requires__.*|\
# ALT: use own package dir\
import site\
site.addsitedir("%certbotdir")|' %buildroot%_bindir/%name

%check
#python_test

%files
%doc LICENSE.txt
%doc README.rst CHANGES.rst CONTRIBUTING.md
%_bindir/%name
#%doc %attr(0644,root,root) %_man1dir/%{name}*
%dir %_sysconfdir/%name/
%dir %_sharedstatedir/%name/
%dir %_logdir/%name/
# compats
%_bindir/letsencrypt
%dir %_sysconfdir/letsencrypt/
%dir %_sharedstatedir/letsencrypt/
%dir %_logdir/letsencrypt/

#files -n python-module-%name
#doc LICENSE.txt
%certbotdir/%name/
%certbotdir/%name-%{version}*.egg-info

%if_with plugins
%files nginx
%doc LICENSE.txt
%certbotdir/certbot_nginx/
%certbotdir/certbot_nginx-%{version}*.egg-info

%files apache
%doc LICENSE.txt
%certbotdir/certbot_apache/
%certbotdir/certbot_apache-%{version}*.egg-info
%endif

%changelog
* Sun Jan 21 2018 Vitaly Lipatov <lav@altlinux.ru> 0.21.0-alt1
- new version 0.21.0 (with rpmrb script)

* Fri Oct 06 2017 Vitaly Lipatov <lav@altlinux.ru> 0.19.0-alt1
- new version 0.19.0 (with rpmrb script)
- drop python-module-cerbot subpackage
- pack nginx and apache plugins

* Tue Aug 08 2017 Vitaly Lipatov <lav@altlinux.ru> 0.14.2-alt1
- new version 0.14.2 (with rpmrb script)

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 0.14.1-alt1
- new version 0.14.1 (with rpmrb script)

* Sat Apr 08 2017 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- new version 0.13.0 (with rpmrb script)

* Fri Mar 10 2017 Terechkov Evgenii <evg@altlinux.org> 0.12.0-alt1
- 0.12.0

* Sun Dec 04 2016 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt1
- new version 0.9.3 (with rpmrb script)

* Fri Oct 07 2016 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- new version 0.9.1 (with rpmrb script)

* Thu Aug 18 2016 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt1
- rename to certbot, build version 0.8.1

* Thu Apr 21 2016 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt1
- new version 0.5.0 (with rpmrb script)

* Fri Mar 18 2016 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt1
- new version 0.4.2 (with rpmrb script)
- fix requires

* Wed Feb 17 2016 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- initial build for ALT Linux Sisyphus

* Thu Feb 11 2016 Nick Bebout <nb@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Thu Jan 28 2016 Nick Bebout <nb@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0
* Sat Jan 23 2016 Robert Buchholz <rbu@fedoraproject.org> - 0.2.0-4
- Use acme dependency version consistently and add psutil min version
* Fri Jan 22 2016 Nick Bebout <nb@fedoraproject.org> - 0.2.0-3
- Update the configargparse version in other places
* Fri Jan 22 2016 Nick Bebout <nb@fedoraproject.org> - 0.2.0-2
- Update python-configargparse version requirement
* Thu Jan 21 2016 Nick Bebout <nb@fedoraproject.org> - 0.2.0-1
- Apache plugin support for non-Debian based systems
- Relaxed PyOpenSSL version requirements
- Resolves issues with the Apache plugin enabling redirect
- Improved error messages from the client
* Wed Dec 16 2015 Nick Bebout <nb@fedoraproject.org> - 0.1.1-2
- Fix packaging issues
* Wed Dec 16 2015 Nick Bebout <nb@fedoraproject.org> - 0.1.1-1
- fix a confusing UI path that caused some users to repeatedly renew their
- certs while experimenting with the client, in some cases hitting issuance rate limits
- numerous Apache configuration parser fixes
- avoid attempting to issue for unqualified domain names like "localhost"
- fix --webroot permission handling for non-root users
* Tue Dec 08 2015 Nick Bebout <nb@fedoraproject.org> - 0.1.0-3
- Add python-sphinx_rtd_theme build requirement
* Fri Dec 04 2015 James Hogarth <james.hogarth@gmail.com> - 0.1.0-2
- Add documentation from upstream
* Thu Dec 03 2015 James Hogarth <james.hogarth@gmail.com> - 0.1.0-1
- Update to new upstream release for the open beta
* Thu Dec 03 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-5.dev20151123
- Add missing build requirements that slipped through
* Wed Dec 02 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-4.dev20151123
- The python2 library should have the dependencies and not the bindir one
* Wed Dec 02 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-3.dev20151123
- Separate out the python libraries from the application itself
- Enable python tests
* Tue Dec 01 2015 James Hogarth <james.hogarth@gmail.com> - 0.0.0-2.dev20151123
- Update spec to account for the runtime dependencies discovered
- Update spec to sit inline with current python practices
* Sun Apr 26 2015 Torrie Fischer <tdfischer@hackerbots.net> 0-1.git1d8281d.fc20
- Initial package
