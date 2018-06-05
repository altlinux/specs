%define  pkgname sass

Name:    ruby-%pkgname
Version: 3.5.6
Release: alt1

Summary: Sass makes CSS fun again.
License: MIT
Group:   Development/Ruby
Url:     https://github.com/sass/sass

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%filter_from_requires /^ruby(compass)/d

%description
Sass makes CSS fun again. Sass is an extension of CSS, adding nested rules,
variables, mixins, selector inheritance, and more. It's translated to
well-formatted, standard CSS using the command line tool or a web-framework
plugin.

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
# fix ROOT_DIR
subst 's|\(ROOT_DIR = "\).*|\1%ruby_sitelibdir/%pkgname"|' %buildroot%ruby_sitelibdir/%pkgname/root.rb
# install VERSION VERSION_NAME
install -m644 VERSION* %buildroot%ruby_sitelibdir/%pkgname

for i in sass sass-convert scss;do
	mv %buildroot%_bindir/{,ruby-}$i
done

%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib test/**/*_test.rb

%files
%doc README*
%_bindir/ruby-sass
%_bindir/ruby-sass-convert
%_bindir/ruby-scss
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 3.5.6-alt1
- Initial build for Sisyphus
