%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
#BuildRequires:  perl(Encode/JP.pm) perl(Catalyst/Action/REST.pm) perl(Test/Most.pm)
BuildRequires:  perl(Encode/JP.pm) perl(Test/Most.pm)
BuildRequires: perl(Catalyst/Helper.pm) perl(Class/Accessor.pm) perl(Class/MOP/Object.pm) perl(Config.pm) perl(Devel/InnerPackage.pm) perl(Encode.pm) perl(Errno.pm) perl(Fcntl.pm) perl(File/Spec/Functions.pm) perl(File/Spec/Unix.pm) perl(FindBin.pm) perl(IO/File.pm) perl(IO/Handle.pm) perl(IO/Socket.pm) perl(IPC/Open3.pm) perl(LWP/Simple.pm) perl(List/Util.pm) perl(Module/Pluggable/Object.pm) perl(Moose/Meta/Class.pm) perl(Moose/Role.pm) perl(Moose/Util.pm) perl(Moose/Util/TypeConstraints.pm) perl(MooseX/MethodAttributes.pm) perl(MooseX/Role/Parameterized.pm) perl(Path/Class/Dir.pm) perl(Path/Class/File.pm) perl(Plack/Loader.pm) perl(Plack/Middleware/Conditional.pm) perl(Plack/Middleware/IIS6ScriptNameFix.pm) perl(Plack/Middleware/IIS7KeepAliveFix.pm) perl(Plack/Middleware/LighttpdScriptNameFix.pm) perl(Plack/Test.pm) perl(Pod/Usage.pm) perl(Term/Size/Any.pm) perl(Tree/Simple/Visitor/FindByUID.pm) perl(URI/QueryParam.pm) perl(URI/http.pm) perl(URI/https.pm) perl(attributes.pm) perl(overload.pm) perl-base perl-devel perl-pod perl-podlators perldoc perl(IO/Scalar.pm) perl(JSON/MaybeXS.pm) perl(Test/Fatal.pm) perl(CGI/Struct.pm) perl(Plack/Middleware/FixMissingBodyInRedirect.pm) perl(Plack/Middleware/MethodOverride.pm) perl(Plack/Middleware/RemoveRedundantBody.pm) perl(Type/Tiny.pm)
# END SourceDeps(oneline)
Name:           perl-Catalyst-Runtime
Summary:        Catalyst Framework Runtime
Version:        5.90117
Release:        alt1
License:        GPL+ or Artistic
Group:          Development/Perl
Source0:        http://www.cpan.org/authors/id/J/JJ/JJNAPIORK/Catalyst-Runtime-%{version}.tar.gz
URL:            http://search.cpan.org/dist/Catalyst-Runtime/
BuildArch:      noarch

BuildRequires:  groff
BuildRequires:  /usr/bin/perldoc
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(CGI/Simple/Cookie.pm)
BuildRequires:  perl(Class/C3/Adopt/NEXT.pm)
BuildRequires:  perl(Class/Data/Inheritable.pm)
BuildRequires:  perl(Class/Load.pm)
BuildRequires:  perl(Class/MOP.pm)
BuildRequires:  perl(CPAN.pm)
BuildRequires:  perl(Data/Dump.pm)
BuildRequires:  perl(Data/OptList.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(HTML/Entities.pm)
BuildRequires:  perl(HTML/HeadParser.pm)
BuildRequires:  perl(HTTP/Body.pm)
BuildRequires:  perl(HTTP/Headers.pm)
BuildRequires:  perl(HTTP/Request.pm)
BuildRequires:  perl(HTTP/Request/AsCGI.pm)
BuildRequires:  perl(HTTP/Request/Common.pm)
BuildRequires:  perl(HTTP/Response.pm)
BuildRequires:  perl(List/MoreUtils.pm)
BuildRequires:  perl(LWP/UserAgent.pm)
BuildRequires:  perl(Module/Pluggable.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(MooseX/Emulate/Class/Accessor/Fast.pm)
BuildRequires:  perl(MooseX/Getopt.pm)
BuildRequires:  perl(MooseX/MethodAttributes/Inheritable.pm)
BuildRequires:  perl(MooseX/Role/WithOverloading.pm)
BuildRequires:  perl(MRO/Compat.pm)
BuildRequires:  perl(namespace/autoclean.pm)
BuildRequires:  perl(namespace/clean.pm)
BuildRequires:  perl(Path/Class.pm)
BuildRequires:  perl(Plack.pm)
BuildRequires:  perl(Plack/Middleware/ReverseProxy.pm)
BuildRequires:  perl(Plack/Test/ExternalServer.pm)
BuildRequires:  perl(Safe/Isa.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(String/RewritePrefix.pm)
BuildRequires:  perl(Sub/Exporter.pm)
BuildRequires:  perl(Task/Weaken.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Text/Balanced.pm)
BuildRequires:  perl(Text/SimpleTable.pm)
BuildRequires:  perl(Time/HiRes.pm)
BuildRequires:  perl(Tree/Simple.pm)
BuildRequires:  perl(Tree/Simple/Visitor/FindByPath.pm)
BuildRequires:  perl(Try/Tiny.pm)
BuildRequires:  perl(URI.pm)

BuildRequires:  perl(Class/Accessor/Fast.pm)
BuildRequires:  perl(Class/C3.pm)
BuildRequires:  perl(Class/Inspector.pm)
BuildRequires:  perl(FCGI.pm)
BuildRequires:  perl(File/Copy/Recursive.pm)
BuildRequires:  perl(File/Modified.pm)
BuildRequires:  perl(Proc/ProcessTable.pm)
BuildRequires:  perl(Test/Harness.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Spelling.pm)
BuildRequires:  perl(Test/Without/Module.pm)
BuildRequires:  perl(YAML.pm)


Requires:       perl(B/Hooks/EndOfScope.pm) >= 0.08
Requires:       perl(CGI/Simple/Cookie.pm) >= 1.109
Requires:       perl(Class/C3/Adopt/NEXT.pm) >= 0.07
Requires:       perl(Class/Load.pm) >= 0.12
Requires:       perl(Class/MOP.pm) >= 0.95
Requires:       perl(HTML/HeadParser.pm)
Requires:       perl(HTTP/Body.pm) >= 1.06
Requires:       perl(HTTP/Headers.pm) >= 1.64
Requires:       perl(HTTP/Request.pm) >= 5.814
Requires:       perl(HTTP/Request/AsCGI.pm) >= 1.0
Requires:       perl(HTTP/Response.pm) >= 5.813
Requires:       perl(LWP/UserAgent.pm)
Requires:       perl(Module/Pluggable.pm) >= 3.9
Requires:       perl(Moose.pm) >= 1.03
Requires:       perl(MooseX/Emulate/Class/Accessor/Fast.pm) >= 0.009.030
Requires:       perl(MooseX/Getopt.pm) >= 0.30
Requires:       perl(MooseX/MethodAttributes/Inheritable.pm) >= 0.24
Requires:       perl(MooseX/Role/WithOverloading.pm) >= 0.09
Requires:       perl(namespace/autoclean.pm) >= 0.09
Requires:       perl(namespace/clean.pm) >= 0.23
Requires:       perl(Path/Class.pm) >= 0.09
Requires:       perl(Plack.pm) >= 0.999.100
Requires:       perl(Plack/Middleware/ReverseProxy.pm) >= 0.04
Requires:       perl(Plack/Test/ExternalServer.pm)
Requires:       perl(String/RewritePrefix.pm) >= 0.004
Requires:       perl(Task/Weaken.pm)
Requires:       perl(Text/SimpleTable.pm) >= 0.03
Requires:       perl(Tree/Simple.pm) >= 1.15
Requires:       perl(URI.pm) >= 1.35

# obolete/provide old tests subpackage
# can be removed during F19 development cycle
Obsoletes:      %{name}-tests < 5.90007-2
Provides:       %{name}-tests = %{version}-%{release}


Source44: import.info

%description
This is the primary class for the Catalyst-Runtime distribution.  It provides
the core of any runtime Catalyst instance.
 
%package        scripts
Summary:        Scripts for %{name}
Group:          Development/Perl
Requires:       %{name} = %{version}-%{release}

%description    scripts

The %{name}-scripts package contains scripts distributed with
%{name} but generally used for developing Catalyst applications.


%prep
%setup -q -n Catalyst-Runtime-%{version}

# something like this seems to beg for explicitness
perldoc perlgpl      > COPYING.gpl
perldoc perlartistic > COPYING.artistic

find .  -type f -exec chmod -c -x {} +
find t/ -type f -exec perl -pi -e 's|^#!perl|#!%{__perl}|' {} +

# timeout
rm -f t/optional*

%build
PERL5_CPANPLUS_IS_RUNNING=1 %{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

# %{_fixperms} %{buildroot}/*

%check
# note that some of the optional tests we're enabling here will be skipped
# anyways, due to deps on Catalyst::Devel, etc.  We cannot depend on
# Catalyst::Devel, however, as it depends on us, and circular dep loops are
# never fun.  (Well, maybe to Zeno.)
#
# See also http://rt.cpan.org/Public/Bug/Display.html?id=27123

export TEST_LIGHTTPD=1
export TEST_HTTP=1

# see https://rt.cpan.org/Public/Bug/Display.html?id=42540
#export TEST_MEMLEAK=1

export TEST_POD=1
export TEST_STRESS=1

make test
make clean

%files
%doc Changes README.mkdn
%{perl_vendor_privlib}/*

%files scripts
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 5.90117-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 5.90115-alt1
- automated CPAN update

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 5.90114-alt1
- automated CPAN update

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 5.90113-alt1
- automated CPAN update

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 5.90111-alt1
- automated CPAN update

* Mon Jun 13 2016 Igor Vlasenko <viy@altlinux.ru> 5.90105-alt1
- automated CPAN update

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 5.90104-alt1
- automated CPAN update

* Fri Nov 13 2015 Igor Vlasenko <viy@altlinux.ru> 5.90103-alt1
- automated CPAN update

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 5.90102-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 5.90101-alt1
- automated CPAN update

* Sat Jan 03 2015 Igor Vlasenko <viy@altlinux.ru> 5.90079-alt1
- automated CPAN update

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 5.90077-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 5.90075-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 5.90071-alt1
- automated CPAN update

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 5.90065-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 5.90064-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 5.90063-alt1
- automated CPAN update

* Tue Apr 22 2014 Igor Vlasenko <viy@altlinux.ru> 5.90062-alt1
- automated CPAN update

* Wed Mar 12 2014 Igor Vlasenko <viy@altlinux.ru> 5.90061-alt1
- automated CPAN update

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 5.90060-alt1
- automated CPAN update

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 5.90053-alt1
- automated CPAN update

* Sun Dec 22 2013 Igor Vlasenko <viy@altlinux.ru> 5.90052-alt1
- automated CPAN update

* Wed Nov 13 2013 Igor Vlasenko <viy@altlinux.ru> 5.90051-alt1
- automated CPAN update

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 5.90042-alt1
- automated CPAN update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 5.90019-alt1_4
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 5.90019-alt1_2
- update to new release by fcimport

* Wed Dec 12 2012 Igor Vlasenko <viy@altlinux.ru> 5.90019-alt1_1
- update to new release by fcimport

* Mon Nov 26 2012 Igor Vlasenko <viy@altlinux.ru> 5.90018-alt1_1
- fixed build by version update

* Tue Oct 23 2012 Igor Vlasenko <viy@altlinux.ru> 5.90017-alt1
- automated CPAN update

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 5.90016-alt1
- automated CPAN update

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 5.90015-alt1
- automated CPAN update

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 5.90002-alt1
- automated CPAN update

* Sun Jan 16 2011 Alexey Tourbin <at@altlinux.ru> 5.80030-alt1
- 5.80024 -> 5.80030

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 5.80024-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun May 16 2010 Alexey Tourbin <at@altlinux.ru> 5.80024-alt1
- 5.80022 -> 5.80024

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 5.80022-alt3
- rebuilt with rpm-build-perl 0.72

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 5.80022-alt2
- re-enabled dependency on Catalyst::Restarter

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 5.80022-alt1
- 5.7015 -> 5.80022
- unit_core_script_test.t: fixed STDIN/STDOUT thinko (rt.cpan.org #56590)
- disabled dependency on Catalyst::Restarter, to facilitate bootstrap

* Sun Dec 14 2008 Michael Bochkaryov <misha@altlinux.ru> 5.7015-alt1
- 5.7015 version
- build requirements updated

* Mon Sep 08 2008 Michael Bochkaryov <misha@altlinux.ru> 5.7014-alt2
- fix directory ownership violation

* Mon Jun 30 2008 Michael Bochkaryov <misha@altlinux.ru> 5.7014-alt1
- 5.7014 version

* Wed Mar 21 2007 Sir Raorn <raorn@altlinux.ru> 5.7006-alt1
- first build for ALT Linux Sisyphus

