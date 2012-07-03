Name: cvs2cl
Version: 2.72
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Generate ChangeLogs from CVS working copies
License: GPLv2+
Group: Development/Other

Url: http://www.red-bean.com/cvs2cl
Source0: %url/cvs2cl.pl
Patch0: cvs2cl-2.67-shebang.patch

BuildArch: noarch

# Automatically added by buildreq on Fri Nov 26 2010
BuildRequires: perl-Pod-Parser

%description
cvs2cl generates GNU-style ChangeLogs for a CVS working copy using the
output of the "cvs log" command.

%prep
%setup -c -T
sed -e 's/cvs2cl\.pl/cvs2cl/' %{SOURCE0} > cvs2cl
%patch0 -p0

%build
pod2man \
 --section=1 --release=%version \
 --center="CVS-log-message-to-ChangeLog conversion script" \
 cvs2cl > cvs2cl.1

%install
install -pD -m755 cvs2cl %buildroot%_bindir/cvs2cl
install -pD -m644 cvs2cl.1 %buildroot%_man1dir/cvs2cl.1

%files
%_bindir/*
%_man1dir/*

%changelog
* Fri Nov 26 2010 Victor Forsiuk <force@altlinux.org> 2.72-alt1
- 2.72

* Wed Jul 30 2008 Victor Forsyuk <force@altlinux.org> 2.71-alt1
- 2.71

* Thu Nov 15 2007 Victor Forsyuk <force@altlinux.org> 2.67-alt1
- Initial build with patches taken from Fedora.
