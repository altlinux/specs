%def_without test

%define module		Set-IntSpan
%define m_distro	Set-IntSpan
%define m_name		Set::IntSpan
Name: perl-%module
Version: 1.16
Release: alt1
Packager: Gleb Stiblo <ulfr@altlinux.ru>

Summary: Set::IntSpan - Manages sets of integers
Summary(ru_RU.KOI8-R): Set::IntSpan - модуль для управления множествами целых чисел
Group: Development/Perl
License: GPL

Url: http://search.cpan.org/dist/%module/
Source: http://www.cpan.org/authors/id/S/SW/SWMCD/Set-IntSpan-1.16.tar.gz

BuildRequires: perl-devel
BuildArch: noarch

%description
Set::IntSpan manages sets of integers.  It is optimized for sets that
have long runs of consecutive integers.  These arise, for example, in
.newsrc files, which maintain lists of articles:

    alt.foo: 1-21,28,31
    alt.bar: 1-14192,14194,14196-14221

Sets are stored internally in a run-length coded form.  This provides
for both compact storage and efficient computation.  In particular,
set operations can be performed directly on the encoded
representation.

%description -l ru_RU.KOI8-R
Set::IntSpan - модуль для управления множествами целых чисел. Он оптимизирован для
множеств включающих большое количество подряд идущих чисел. К примеру:

    alt.foo: 1-21,28,31
    alt.bar: 1-14192,14194,14196-14221

Внутренний формат хранения компактен и обеспечивает эффективные вычисления.
В частности, операции над множествами могут быть выполнены прямо над внутренним
представлении.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Set
%doc README

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- automated CPAN update

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Sep 04 2008 Gleb Stiblo <ulfr@altlinux.ru> 1.13-alt1
- fixes for repocop warns
- new version

* Wed Sep 26 2007 Gleb Stiblo <ulfR@altlinux.ru> 1.12-alt1
- added support for spans in constructors

* Thu May 24 2007 Gleb Stiblo <ulfR@altlinux.ru> 1.11-alt1
- new version

* Tue May 23 2006 Gleb Stiblo <ulfR@altlinux.ru> 1.09-alt1
- added indexing methods
- 'die' instead of 'craok' on fatal errors

* Tue Dec 21 2004 Gleb Stiblo <ulfR@altlinux.ru> 1.08-alt1
- new release

* Mon May 03 2004 Gleb Stiblo <ulfr@altlinux.ru> 1.07-alt2
- glibc 2.3 build

* Tue Mar 23 2004 Gleb Stiblo <ulfr@altlinux.ru> 1.07-alt1
- ALT adaptations.

