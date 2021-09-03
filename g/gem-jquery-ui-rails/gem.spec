%define        gemname jquery-ui-rails

Name:          gem-jquery-ui-rails
Version:       6.0.1
Release:       alt1.1
Summary:       jQuery UI for the Rails asset pipeline
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jquery-ui-rails/jquery-ui-rails
Vcs:           https://github.com/jquery-ui-rails/jquery-ui-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(railties) >= 3.2.16
BuildRequires: gem(json) >= 2.0 gem(json) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names testapp
Requires:      gem(railties) >= 3.2.16
Provides:      gem(jquery-ui-rails) = 6.0.1


%description
This gem packages the jQuery UI assets (JavaScripts, stylesheets, and images)
for the Rails asset pipeline, so you never have to download a custom package
through the web interface again.

See VERSIONS.md to see which versions of jquery-ui-rails bundle which versions
of jQuery UI.

Warning: This gem is incompatible with the jquery-rails gem before version
3.0.0! Strange things will happen if you use an earlier jquery-rails version.
Run bundle list to ensure that you either aren't using jquery-rails, or at least
version 3.0.0 of jquery-rails.


%package       -n gem-jquery-ui-rails-doc
Version:       6.0.1
Release:       alt1.1
Summary:       jQuery UI for the Rails asset pipeline documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета jquery-ui-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(jquery-ui-rails) = 6.0.1

%description   -n gem-jquery-ui-rails-doc
jQuery UI for the Rails asset pipeline documentation files.

This gem packages the jQuery UI assets (JavaScripts, stylesheets, and images)
for the Rails asset pipeline, so you never have to download a custom package
through the web interface again.

See VERSIONS.md to see which versions of jquery-ui-rails bundle which versions
of jQuery UI.

Warning: This gem is incompatible with the jquery-rails gem before version
3.0.0! Strange things will happen if you use an earlier jquery-rails version.
Run bundle list to ensure that you either aren't using jquery-rails, or at least
version 3.0.0 of jquery-rails.

%description   -n gem-jquery-ui-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета jquery-ui-rails.


%package       -n gem-jquery-ui-rails-devel
Version:       6.0.1
Release:       alt1.1
Summary:       jQuery UI for the Rails asset pipeline development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета jquery-ui-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(jquery-ui-rails) = 6.0.1
Requires:      gem(json) >= 2.0 gem(json) < 3

%description   -n gem-jquery-ui-rails-devel
jQuery UI for the Rails asset pipeline development package.

This gem packages the jQuery UI assets (JavaScripts, stylesheets, and images)
for the Rails asset pipeline, so you never have to download a custom package
through the web interface again.

See VERSIONS.md to see which versions of jquery-ui-rails bundle which versions
of jQuery UI.

Warning: This gem is incompatible with the jquery-rails gem before version
3.0.0! Strange things will happen if you use an earlier jquery-rails version.
Run bundle list to ensure that you either aren't using jquery-rails, or at least
version 3.0.0 of jquery-rails.

%description   -n gem-jquery-ui-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета jquery-ui-rails.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-jquery-ui-rails-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-jquery-ui-rails-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 6.0.1-alt1.1
- ! spec

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 6.0.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
