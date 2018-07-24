%define  pkgname archive-zip

Name:    ruby-%pkgname
Version: 0.11.0
Release: alt1

Summary: A simple Ruby-esque interface to creating, extracting, and updating ZIP archives in 100% Ruby.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/javanthropus/archive-zip

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
Simple, extensible, pure Ruby ZIP archive support.

Basic archive creation and extraction can be handled using only a few
methods. More complex operations involving the manipulation of existing
archives in place (adding, removing, and modifying entries) are also
possible with a little more work. Even adding advanced features such as
new compression codecs are supported with a moderate amount of effort.

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.11.0-alt1
- Initial build for Sisyphus
