Name: s3cmd
Version: 1.1.0
Release: alt1.beta3
License: GPL

Group: Networking/Other

Source: %name-%version-%release.tar
# Automatically added by buildreq on Fri Nov 14 2008
BuildRequires: python-devel python-modules-xml
BuildArch: noarch
Summary: S3cmd is a tool for managing Amazon S3 storage space

%description
S3cmd lets you copy files from/to Amazon S3
(Simple Storage Service) using a simple to use
command line client.
Features include 'sync' command for rsync-like
directory tree synchronization.

%prep
%setup -q -n %name-%version-%release

%build
%python_build

%install
%python_install

%files
%doc INSTALL NEWS README
%_bindir/*
%_man1dir/*.1*
%python_sitelibdir/*
%exclude %_docdir/packages/

%changelog
* Sun Mar 11 2012 Yuriy Kashirin <uka@altlinux.ru> 1.1.0-alt1.beta3
- New version
- Updated gear repository from upstream git
- Use fixed "/usr/bin/gpg" path instead of find_executable from
  distutils, prevents dependency on devel packages (fixes #26917)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt0.rc2.1
- Rebuild with Python-2.7

* Wed Dec 15 2010 Yuriy Kashirin <uka@altlinux.ru> 1.0.0-alt0.rc2
- New version
- Updated gear repository from upstream svn

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.4-alt1.1
- Rebuilt with python 2.6

* Fri Nov 14 2008 Veaceslav Grecea <slavutich@altlinux.org> 0.9.8.4-alt1
- Ported to ALT

* Tue Sep 16 2008 - michal@logix.cz
- Upgrade to s3cmd 0.9.8.4
  - Restored access to upper-case named buckets.
  - Improved handling of filenames with Unicode characters.
  - Avoid ZeroDivisionError on ultrafast links (for instance
    on Amazon EC2)
