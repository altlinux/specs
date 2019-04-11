%define  pkgname thin

Name:    gem-%pkgname
Version: 1.7.2
Release: alt1

Summary: A very fast & simple Ruby web server
License: GPLV2+
Group:   Development/Ruby
Url:     https://github.com/macournoyer/thin

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>

# VCS:   https://github.com/macournoyer/thin
Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%add_findprov_skiplist %ruby_gemlibdir/example/*
%add_findreq_skiplist %ruby_gemlibdir/example/*

%add_findprov_skiplist %ruby_gemlibdir/lib/thin/controllers/service.sh.erb
%add_findreq_skiplist %ruby_gemlibdir/lib/thin/controllers/service.sh.erb

%description
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %name-%version

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc *.md
%_bindir/%pkgname
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files doc
%ruby_gemdocdir

%changelog
* Thu Apr 11 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.7.2-alt1
- Initial build for Sisyphus
