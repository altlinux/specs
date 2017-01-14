%define _unpackaged_files_terminate_build 1
%define dist Lingua-EN-Tagger
Name: perl-%dist
Version: 0.28
Release: alt1

Summary: Part-of-speech tagger for English natural language processing
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/A/AC/ACOBURN/%{dist}-%{version}.tar.gz

Patch: perl-Lingua-EN-Tagger-0.23-alt-nstore.patch

BuildArch: noarch

# cannot be deduced automatically
Requires: perl-Memoize-ExpireLRU

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: perl-HTML-Parser perl-Lingua-Stem perl-Memoize-ExpireLRU perl-devel

%description
The module is a probability based, corpus-trained tagger that assigns POS tags
to English text based on a lookup dictionary and a set of probability values.
The tagger assigns appropriate tags based on conditional probabilities - it
examines the preceding tag to determine the appropriate tag for the current
word.  Unknown words are classified according to word morphology or can be set
to be treated as nouns or other parts of speech.

%prep
%setup -q -n %{dist}-%{version}
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Lingua*

%changelog
* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- automated CPAN update

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 0.20-alt1
- 0.16 -> 0.20

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Tue Apr 27 2010 Alexey Tourbin <at@altlinux.ru> 0.15-alt3
- Makefile.PL: changed Storable::store() to nstore() for noarch data

* Tue Apr 27 2010 Alexey Tourbin <at@altlinux.ru> 0.15-alt2
- Tagger.pm: changed Storable::store() to nstore() for noarch data

* Tue Apr 27 2010 Alexey Tourbin <at@altlinux.ru> 0.15-alt1
- initial revision
