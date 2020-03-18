%define        pkgname activemodel-serializers-xml

Name:          gem-%pkgname
Version:       1.0.2
Release:       alt2
Summary:       This gem provides XML serialization for your Active Model objects and Active Record models
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/activemodel-serializers-xml/
Vcs:           https://github.com/rails/activemodel-serializers-xml.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
%summary.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Fri Mar 06 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt2
- > Ruby Policy 2.0
- ! spec tags

* Tue Oct 02 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
