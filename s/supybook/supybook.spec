Name: supybook
Version: 0.0.3
Release: alt1

Summary: The Supybot handbook
Group: Documentation
License: GPLv3
Url: http://supybook.fealdia.org/

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

BuildArch: noarch

# git://repo.or.cz/supybook.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: asciidoc >= 8.2 python-modules-encodings

%description
This document is a handbook for Supybot, the IRC (Internet Relay Chat)
bot written in Python.

%prep
%setup
%patch -p1

%build
%make_build VERSION=%version

%files
%doc index.html

%changelog
* Wed Jan 13 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.0.3-alt1
- v0.0.2-9-gc38f6d1

* Sun Oct 05 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.0.2-alt1
- initial build
