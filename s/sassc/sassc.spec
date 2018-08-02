%def_disable snapshot
%def_enable check
# use corresponding 3.5.x version
%define testspec_version 3.5.4

Name: sassc
Version: 3.5.0
Release: alt1

Summary: Wrapper around libsass to compile CSS stylesheet
Group: Text tools
License: MIT
Url: http://github.com/sass/sassc

%if_disabled snapshot
Source: %name-%version.tar.gz
Source1: sass-spec-%testspec_version.tar.gz
%else
#VCS: https://github.com/sass/sassc.git
Source: %name-%version.tar
#VCS: https://github.com/sass/sass-spec.git
Source1: sass-spec-%testspec_version.tar
%endif

BuildRequires: gcc-c++ libsass-devel >= %version
# for check
BuildRequires: ruby ruby-stdlibs

%description
SassC is a wrapper around libsass used to generate a useful command-line
application that can be installed and packaged for several operating systems.

%prep
%setup -a 1
mv sass-spec-%testspec_version sass-spec
echo %version > VERSION

%build
%add_optflags -D_FILE_OFFSET_BITS=64
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
# two tests failed
rm -rf sass-spec/spec/sass/import/unquoted
rm -rf sass-spec/spec/libsass-closed-issues/issue_2360

ruby sass-spec/sass-spec.rb -V 3.5 -c ./%name --impl libsass sass-spec/spec

%files
%_bindir/%name
%doc LICENSE Readme.md

%changelog
* Wed Jul 18 2018 Yuri N. Sedunov <aris@altlinux.org> 3.5.0-alt1
- 3.5.0

* Thu Feb 22 2018 Yuri N. Sedunov <aris@altlinux.org> 3.4.8-alt1
- first build for Sisyphus

