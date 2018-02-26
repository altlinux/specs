Name:		jargon-html
Version:	4.4.7
Release:	alt1
Summary:	The Jargon File
URL:		http://catb.org/jargon/index.html
Group:		Documentation
License:	Distributable
Source:		jargon-%version.tar.gz
BuildArch:	noarch

%description
This is the Jargon File, a comprehensive compendium of hacker slang
illuminating many aspects of hackish tradition, folklore, and humor.

%prep
%setup -n jargon-%version

%files
%doc .


%changelog
* Thu Sep 22 2011 Fr. Br. George <george@altlinux.ru> 4.4.7-alt1
- Initial build from scratch (HTML tarball)

