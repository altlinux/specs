%define rname p6014
%define what content
Name: %rname-%what
Version: 0.2.1
Release: alt1

Group: Games/Adventure
Summary: Game data for %rname package
Url: http://code.google.com/p/project6014/
License: May be copied freely as part of %rname

Buildarch: noarch

Requires: %rname-common

Source0: P6014-%version-prv-%what.uqm

%description
This package contains the non-hires %what data required for the %rname package.

Copyright :
The content -- voiceovers, dialogue, graphics, and music -- are
copyright (C) 1992, 1993, 2002 Toys for Bob, Inc. or their
respective creators.  The content may be copied freely as part of
a distribution of The Ur-Quan Masters.  All other rights are reserved.

%prep
%setup -c -T

%install
mkdir -p %buildroot/%_gamesdatadir/%rname/content/packages
install -m0644 %SOURCE0 %buildroot/%_gamesdatadir/%rname/content/packages/

cat >>copyright << __EOF__
Copyright :
The content -- voiceovers, dialogue, graphics, and music -- are
copyright (C) 1992, 1993, 2002 Toys for Bob, Inc. or their
respective creators.  The content may be copied freely as part of
a distribution of The Ur-Quan Masters.  All other rights are reserved.
__EOF__

%files
%doc copyright
%_gamesdatadir/%rname/content/packages/*.uqm

%changelog
* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1
- initial spec
