%define ver_major 3.6

%def_disable snapshot
%def_enable spec_snapshot
%def_enable check
# use corresponding 3.6.x version
%define testspec_version %ver_major.3

Name: sassc
Version: %ver_major.2
Release: alt1.1

Summary: Wrapper around libsass to compile CSS stylesheet
Group: Text tools
License: MIT
Url: http://github.com/sass/sassc

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
Vcs: https://github.com/sass/sassc.git
Source: %name-%version.tar
%endif

%if_disabled spec_snapshot
Source1: https://github.com/sass/sass-spec/archive/libsass-%testspec_version/sass-spec-libsass-%testspec_version.tar.gz
%else
Vcs: https://github.com/sass/sass-spec.git
Source1: sass-spec-%testspec_version.tar
%endif
Patch1: sassc-3.6.2-alt-file_exists.patch

BuildRequires: gcc-c++ libsass-devel >= %version
%{?_enable_check:BuildRequires: ruby-minitest gem-hrx gem-file_exists}

%description
SassC is a wrapper around libsass used to generate a useful command-line
application that can be installed and packaged for several operating systems.

%prep
%setup -a 1
mv sass-spec-%{?_disable_spec_snapshot:libsass-}%testspec_version sass-spec
echo %version > VERSION

%patch1 -b .file_exists

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
ruby sass-spec/sass-spec.rb --impl libsass -c ./%name

%files
%_bindir/%name
%doc LICENSE Readme.md

%changelog
* Wed Aug 14 2024 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1.1
- fixed %%check for Ruby >= 3.2

* Mon Jun 07 2021 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2
- updated sassc-spec to 3.6.3-255-ge6a5b525

* Wed Dec 09 2020 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt2
- updated sassc-spec to 3.6.3-164-g6015399e
  to make check happy against libsass-3.6.4

* Fri Aug 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Wed Jul 18 2018 Yuri N. Sedunov <aris@altlinux.org> 3.5.0-alt1
- 3.5.0

* Thu Feb 22 2018 Yuri N. Sedunov <aris@altlinux.org> 3.4.8-alt1
- first build for Sisyphus

