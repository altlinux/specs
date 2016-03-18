Name: letsencrypt
Version: 0.4.2
Release: alt1

Summary: A free, automated certificate authority client

License: ASL 2.0
Group: Networking/Other
Url: https://letsencrypt.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.python.org/packages/source/l/%name/%name-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-devel python-module-distribute

Requires: python-module-letsencrypt = %version-%release

Requires: python-module-zope.component
Requires: python-module-zope.interface >= 4.1.0
Requires: python-module-pyasn1
Requires: dialog
# Due Prior to Python 2.7.9 the stdlib SSL module did not allow a user to configure
# See /usr/lib/python2.7/site-packages/acme/client.py
Requires: python-base >= 2.7.9

# Required for documentation
#BuildRequires: python-sphinx
#BuildRequires: python-sphinx_rtd_theme
#BuildRequires: python-repoze-sphinx-autointerface
#BuildRequires: python-sphinxcontrib-programoutput

#Require for testing
#BuildRequires: python-nose-xcover
#BuildRequires: python-pep8
#BuildRequires: python-tox
#BuildRequires: python-mock
#BuildRequires: python-configargparse >= 0.10.0
#BuildRequires: python-zope-interface
#BuildRequires: python-zope-component
#BuildRequires: python-requests
#BuildRequires: python2-dialog >= 3.3.0
#BuildRequires: python-psutil >= 2.1.0
#BuildRequires: python-parsedatetime
#BuildRequires: python-configobj
#BuildRequires: python2-configargparse >= 0.10.0
#BuildRequires: python2-acme = %version

%description
Let's Encrypt is a free, automated certificate authority that aims
to lower the barriers to entry for encrypting all HTTP traffic on the internet.

%package -n python-module-letsencrypt
Group: Networking/Other
Requires: python-module-configargparse >= 0.10.0
Requires: python-module-dialog >= 3.3.0
Requires: python-module-psutil >= 2.1.0
Requires: python-module-acme = %version
#Recommends: letsencrypt-doc
Summary: Python 2 libraries used by letsencrypt

%description -n python-module-letsencrypt
The python2 libraries to interface with letsencrypt.

#%package doc
#Provides: bundled(jquery)
#Provides: bundled(underscore)
#Provides: bundled(inconsolata-fonts)
#Provides: bundled(lato-fonts)
#Provides: bundled(robotoslab-fonts)
#Requires: fontawesome-fonts fontawesome-fonts-web
#Summary:  Documentation for the reference letsencrypt client

#%description doc
#Documentation for the reference letsencrypt client and libraries

%prep
%setup

%build
# We are using letsencrypt and not supporting letsencrypt-auto
%__subst 's/letsencrypt-auto/letsencrypt/g' letsencrypt/cli.py
%python_build

# build documentation
#%__python setup.py install --user
#make -C docs html man PATH=${HOME}/.local/bin:$PATH

# Clean up stuff we don't need fof docs
#rm -rf docs/_build/html/{.buildinfo,_sources}

%install
%python_install

# Unbundle fonts already on system and put the html docs in place
# Lato ttf is in texlive but that adds a lot of dependencies (30+MB) for just a font in documentation
# and lato is not in it's own -fonts package, only texlive
#rm -f docs/_build/html/_static/fonts/fontawesome*
#ln -sf %_datadir/fonts/fontawesome/fontawesome-webfont.eot docs/_build/html/_static/fonts/fontawesome-webfont.eot
#ln -sf %_datadir/fonts/fontawesome/fontawesome-webfont.svg docs/_build/html/_static/fonts/fontawesome-webfont.svg
#ln -sf %_datadir/fonts/fontawesome/fontawesome-webfont.ttf docs/_build/html/_static/fonts/fontawesome-webfont.ttf
#ln -sf %_datadir/fonts/fontawesome/fontawesome-webfont.woff docs/_build/html/_static/fonts/fontawesome-webfont.woff

# Put the man pages in place
#install -pD -t %buildroot%_man1dir docs/_build/man/*1*

mkdir -p %buildroot%_sysconfdir/%name
mkdir -p %buildroot%_sharedstatedir/%name
mkdir -p %buildroot%_logdir/%name

%check
#python_test

%files
%doc LICENSE.txt
%doc README.rst CHANGES.rst CONTRIBUTING.md
%_bindir/letsencrypt
#%doc %attr(0644,root,root) %_man1dir/%{name}*
%dir %_sysconfdir/%name/
%dir %_sharedstatedir/%name/
%dir %_logdir/%name/

%files -n python-module-letsencrypt
%doc LICENSE.txt
%python_sitelibdir/%name
%python_sitelibdir/%name-%{version}*.egg-info

#%files doc
#%license LICENSE.txt
#%doc docs/_build/html

%changelog
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
