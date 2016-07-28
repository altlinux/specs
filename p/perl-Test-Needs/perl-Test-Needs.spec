# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(IPC/Open3.pm) perl(Test/More.pm) perl(Test2/Event.pm)
# END SourceDeps(oneline)
%define module_version 0.002002
%define module_name Test-Needs
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.002002
Release: alt2
Summary: Skip tests when modules not available
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/H/HA/HAARG/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
Skip test scripts if modules are not available.  The requested modules will be
loaded, and optionally have their versions checked.  If the module is missing,
the test script will be skipped.  Modules that are found but fail to compile
will exit with an error rather than skip.

If used in a subtest, the remainder of the subtest will be skipped.

Skipping will work even if some tests have already been run, or if a plan has
been declared.

Versions are checked via a `$module->VERSION($wanted_version)' call.
Versions must be provided in a format that will be accepted.  No extra
processing is done on them.

If `perl' is used as a module, the version is checked against the running perl
version ($]).  The version can be specified as a number,
dotted-decimal string, v-string, or version object.

If the `RELEASE_TESTING' environment variable is set, the tests will fail
rather than skip.  Subtests will be aborted, but the test script will continue
running after that point.
%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/T*

%changelog
* Thu Jul 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.002002-alt2
- to Sisyphus

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.002002-alt1
- initial import by package builder

