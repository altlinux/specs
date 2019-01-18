%define  pkgname did-you-mean

Name:    gem-%pkgname
Version: 1.3.0
Release: alt1

Summary: The gem that has been saving people from typos since 2014
License: MIT
Group:   Development/Ruby
Url:     https://github.com/yuki24/did_you_mean
# VCS:   https://github.com/yuki24/did_you_mean.git

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
mkdir -p %buildroot%rubygem_gemdir/%pkgname-%version/lib/
mv %buildroot%ruby_sitelibdir/* %buildroot%rubygem_gemdir/%pkgname-%version/lib/

%check
%rake_test

%files
%doc *.md
%rubygem_gemdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Thu Jan 17 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus
