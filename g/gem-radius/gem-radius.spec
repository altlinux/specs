%define        gemname radius

Name:          gem-radius
Version:       0.8.0
Release:       alt0.1
Summary:       Small, but powerful tag-based template language for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jlong/radius
Vcs:           https://github.com/jlong/radius.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(radius) = 0.8.0


%description
Radius is a powerful tag-based template language for Ruby inspired by the
template languages used in MovableType and TextPattern. It uses tags similar to
XML, but can be used to generate any form of plain text (HTML, e-mail, etc).


%package       -n gem-radius-doc
Version:       0.8.0
Release:       alt0.1
Summary:       Small, but powerful tag-based template language for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета radius
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(radius) = 0.8.0

%description   -n gem-radius-doc
Small, but powerful tag-based template language for Ruby documentation
files.

Radius is a powerful tag-based template language for Ruby inspired by the
template languages used in MovableType and TextPattern. It uses tags similar to
XML, but can be used to generate any form of plain text (HTML, e-mail, etc).

%description   -n gem-radius-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета radius.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-radius-doc
%doc README.rdoc
%ruby_gemdocdir


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt0.1
- ^ 0.7.5 -> 0.8.0

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.5-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
