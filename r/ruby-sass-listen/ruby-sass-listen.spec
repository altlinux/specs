%define  pkgname sass-listen

Name:    ruby-%pkgname
Version: 4.0.0
Release: alt2.1

Summary: The Listen gem listens to file modifications and notifies you about the changes
License: MIT
Group:   Development/Ruby
Url:     https://github.com/sass/listen

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar
Patch1: ruby-listen-alt-no-git.patch

BuildRequires(pre): rpm-build-ruby

%description
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

Requires: %name = %EVR

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%patch1 -p1
sed -i '/rb-fsevent/d' %pkgname.gemspec
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
#pushd .%pkgname
#ruby -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
#popd

%files
%doc README.md CHANGELOG.md CONTRIBUTING.md
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Sep 05 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt2.1
- Rebuild for new Ruby autorequirements.
- Simplify spec.
- Disable tests.

* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 4.0.0-alt2
- Rebuild as ruby gem for openqa

* Tue Jun 05 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus
