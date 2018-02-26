Name: tailor
Version: 0.9.27
Release: alt1.1.1.1

Summary: Migrate changesets between SCMs
License: GPL
Group: Development/Other
URL: http://www.darcs.net/DarcsWiki/Tailor
Packager: Alexey Tourbin <at@altlinux.ru>

Source: %name-%version-%release.tar

BuildArch: noarch

Requires: python = %__python_version
BuildPreReq: python-devel = %__python_version

%description
Tailor is a tool to migrate changesets between ArX, Bazaar, Bazaar-NG, CVS,
Codeville, Darcs, Git, Mercurial, Monotone, Subversion and Tla repositories.

%prep
%setup -q -n %name-%version-%release

%build
%__python setup.py build

%install
%__python setup.py install --root=%buildroot --optimize=2

%files
%doc README*
%_bindir/tailor
%python_sitelibdir/vcpx/

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.27-alt1.1.1.1
- Rebuild with Python-2.7

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.27-alt1.1.1
- Rebuilt with python 2.6

* Mon Feb 11 2008 Grigory Batalov <bga@altlinux.ru> 0.9.27-alt1.1
- Rebuilt with python-2.5.

* Sat Jan 13 2007 Alexey Tourbin <at@altlinux.ru> 0.9.27-alt1
- initial revision
