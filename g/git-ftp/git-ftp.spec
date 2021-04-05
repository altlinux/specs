Name: git-ftp
Version: 1.6.0
Release: alt1

Summary: Git powered FTP client written as shell script
License: GPLv3
Group: Development/Other
Url: https://github.com/git-ftp
BuildArch: noarch
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source: %name-%version.tar.gz
Patch0: fix-mans.patch
Requires:	git
Requires:	curl	

BuildRequires: pandoc man-db

%description
Git powered FTP client written as shell script.

%prep
%setup
#patch0 -p2

%build

%install
#makeinstall install-all
make install-all  bindir=%{buildroot}%{_bindir} mandir=%{buildroot}%{_mandir}/man1


%files
%_bindir/git-ftp
%_man1dir/git-ftp.1*

%changelog
* Mon Apr 05 2021 Ilya Mashkin <oddity@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Wed Mar 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1.1
- NMU: added URL

* Sun Aug 12 2012 Paul Wolneykien <manowar@altlinux.ru> 0.8.0-alt1
- Initial build for ALT Linux.
