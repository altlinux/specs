%def_enable snapshot
%def_enable check
# use latest 3.4.x version
%define testspec_version 3.4.3

Name: sassc
Version: 3.4.8
Release: alt1

Summary: Wrapper around libsass to compile CSS stylesheet
Group: Text tools
License: MIT
Url: http://github.com/sass/sassc

#VCS: https://github.com/sass/sassc.git
Source: %name-%version.tar
#VCS: https://github.com/sass/sass-spec.git
Source1: sass-spec-%testspec_version.tar

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
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
ruby sass-spec/sass-spec.rb -V 3.4 -c ./%name --impl libsass sass-spec/spec

%files
%_bindir/%name
%doc LICENSE Readme.md

%changelog
* Thu Feb 22 2018 Yuri N. Sedunov <aris@altlinux.org> 3.4.8-alt1
- first build for Sisyphus

