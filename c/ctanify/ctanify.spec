Name: ctanify
Version: 1.1
Release: alt1.1

Summary: Prepare a package for upload to CTAN
License: LPPL
Group: Development/Other

Url: http://tug.ctan.org/cgi-bin/ctanPackageInformation.py?id=ctanify
Packager: Kirill Maslinsky <kirill@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: rpm-build-perl
BuildRequires: perl-devel

Requires: zip tar
BuildRequires: perl-Pod-Parser

%description 
Given a list of filenames, ctanify creates a tarball (a .tar.gz
file) with the files laid out in CTAN's preferred structure.  The tarball
additionally contains a ZIP (.zip) file with copies of all files laid out in
the standard TeX Directory Structure (TDS), which may be used by those
intending to install the package, or by those who need to incorporate it in a
distribution.  (The TDS ZIP file will be installed in the CTAN install/ tree.)

%prep
%setup

%build

%install
install -D -m 755 ctanify %buildroot%_bindir/ctanify
install -D -m 644 ctanify.1 %buildroot%_man1dir/ctanify.1

%files
%_bindir/*
%_man1dir/*
%doc ctanify.pdf README


%changelog
* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Nov 19 2009 Kirill Maslinsky <kirill@altlinux.org> 1.1-alt1
- updated to 1.1
- drop tdsoutdir patch (applied upstream)

* Mon May 18 2009 Kirill Maslinsky <kirill@altlinux.org> 1.0-alt1
- Initial build for ALT Linux Sisyphus

