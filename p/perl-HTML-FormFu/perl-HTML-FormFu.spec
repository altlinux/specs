# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Catalyst.pm) perl(Catalyst/Helper.pm) perl(Catalyst/Model/DBIC/Schema.pm) perl(Catalyst/Runtime.pm) perl(Catalyst/Test.pm) perl(Catalyst/View/TT.pm) perl(Config.pm) perl(DBIx/Class.pm) perl(DBIx/Class/Schema.pm) perl(Data/Dumper.pm) perl(Exporter.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(FindBin.pm) perl(IO/Handle.pm) perl(List/Util.pm) perl(Pod/Usage.pm) perl(Regexp/Assemble.pm) perl(overload.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(Encode/JP.pm)
Name:           perl-HTML-FormFu
Version:        0.09010
Release:        alt2_1
Summary:        HTML Form Creation, Rendering and Validation Framework
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/HTML-FormFu/
Source0:        http://search.cpan.org/CPAN/authors/id/C/CF/CFRANKS/HTML-FormFu-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Captcha/reCAPTCHA.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(CGI.pm)
BuildRequires:  perl(CGI/Simple.pm)
BuildRequires:  perl(Class/Accessor/Chained/Fast.pm)
BuildRequires:  perl(Class/MOP/Method.pm)
BuildRequires:  perl(Clone.pm)
BuildRequires:  perl(Config/Any.pm)
BuildRequires:  perl(Crypt/CBC.pm)
BuildRequires:  perl(Crypt/DES.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(Data/Visitor.pm)
BuildRequires:  perl(Data/Visitor/Callback.pm)
BuildRequires:  perl(Date/Calc.pm)
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DateTime/Format/Builder.pm)
BuildRequires:  perl(DateTime/Format/Natural.pm)
BuildRequires:  perl(DateTime/Format/Strptime.pm)
BuildRequires:  perl(DateTime/Locale.pm)
BuildRequires:  perl(Email/Valid.pm)
BuildRequires:  perl(Encode.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Fatal.pm)
BuildRequires:  perl(File/Copy.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/ShareDir.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(Hash/Flatten.pm)
BuildRequires:  perl(HTML/Scrubber.pm)
BuildRequires:  perl(HTML/TokeParser/Simple.pm)
BuildRequires:  perl(HTTP/Headers.pm)
BuildRequires:  perl(IO/File.pm)
BuildRequires:  perl(List/MoreUtils.pm)
BuildRequires:  perl(Locale/Maketext.pm)
BuildRequires:  perl(Module/Pluggable.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(Moose/Role.pm)
BuildRequires:  perl(Moose/Util.pm)
BuildRequires:  perl(MooseX/Aliases.pm)
BuildRequires:  perl(MooseX/Attribute/Chained.pm)
BuildRequires:  perl(MooseX/SetOnce.pm)
BuildRequires:  perl(Number/Format.pm)
BuildRequires:  perl(Path/Class/File.pm)
BuildRequires:  perl(POSIX.pm)
BuildRequires:  perl(Readonly.pm)
BuildRequires:  perl(Regexp/Common.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Storable.pm)
BuildRequires:  perl(Task/Weaken.pm)
BuildRequires:  perl(Template.pm)
BuildRequires:  perl(Test/Aggregate/Nested.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(YAML/XS.pm)
Requires:       perl(Captcha/reCAPTCHA.pm) >= 0.93
Requires:       perl(Class/Accessor/Chained/Fast.pm)
Requires:       perl(Config/Any.pm) >= 0.18
Requires:       perl(Crypt/DES.pm)
Requires:       perl(Data/Visitor.pm) >= 0.26
Requires:       perl(Date/Calc.pm)
Requires:       perl(DateTime.pm) >= 0.38
Requires:       perl(DateTime/Format/Builder.pm) >= 0.80
Requires:       perl(HTML/TokeParser/Simple.pm) >= 3.14
Requires:       perl(HTTP/Headers.pm) >= 1.64
Requires:       perl(MooseX/Attribute/Chained.pm) >= 1.0.1
Requires:       perl(Template.pm)
Requires:       perl(YAML/XS.pm) >= 0.32

%{echo 
%filter_from_provides /perl(unicode/d
%filter_from_requires /perl.Catalyst/d; /perl(default/d; /perl(model_config.pm./d;

}
Source44: import.info

%description
HTML::FormFu is a HTML form framework which aims to be as easy as possible
to use for basic web forms, but with the power and flexibility to do
anything else you might want to do (as long as it involves forms).

%prep
%setup -q -n HTML-FormFu-%{version}

find examples -type f | xargs chmod 644
find examples -type f | xargs sed -i -e 's/\r//'


%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

rm -rf $RPM_BUILD_ROOT/blib


%check
#make test

%files
%doc Changes README examples
%{perl_vendor_privlib}/*
%{_bindir}/*.pl
%{_mandir}/man1/*

%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.09010-alt2_1
- moved to Sisyphus (Tapper dep) - bootstrap

* Mon Oct 15 2012 Igor Vlasenko <viy@altlinux.ru> 0.09010-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.09007-alt1_3
- update to new release by fcimport

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.09007-alt1_1
- fc import

