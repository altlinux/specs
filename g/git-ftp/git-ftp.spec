Name: git-ftp
Version: 0.8.0
Release: alt1.1

Summary: Git powered FTP client written as shell script
License: GPLv3
Group: Development/Other
Url: https://github.com/git-ftp
BuildArch: noarch

Source: %name-%version.tar
Patch0: fix-mans.patch

BuildRequires: pandoc

%description
Git powered FTP client written as shell script.

%prep
%setup
%patch0 -p2

%build

%install
%makeinstall install-all

%files
%_bindir/git-ftp
%_man1dir/git-ftp.1*

%changelog
* Wed Mar 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1.1
- NMU: added URL

* Sun Aug 12 2012 Paul Wolneykien <manowar@altlinux.ru> 0.8.0-alt1
- Initial build for ALT Linux.
