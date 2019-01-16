%define  pkgname yard

Name:    ruby-%pkgname
Version: 0.9.16
Release: alt1

Summary: YARD is a Ruby Documentation tool. The Y stands for "Yay!"
License: MIT
Group:   Development/Ruby
Url:     https://yardoc.org/
# VCS:   https://github.com/lsegal/yard.git

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%package -n yard
Summary: Yard, Yardoc, and Yri executables for yard gem
Group: Documentation

BuildArch: noarch
Requires: %name = %version-%release

%description -n yard
%summary.

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
#%rake_spec

%files
%doc *.md
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%files -n yard
%_bindir/*

%changelog
* Sat Dec 29 2018 Pavel Skrylev <majioa@altlinux.org> 0.9.16-alt1
- Initial build for Sisyphus, packaged as a gem
