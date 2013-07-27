%define node_module typescript

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name:           node-%node_module
Version:        0.9.0.1
Release:        alt1
Summary:        TypeScript is a language for application scale JavaScript development
License:        Apache License 2.0
Group:          Development/Other
URL:            http://www.typescriptlang.org
Source0:        http://registry.npmjs.org/%{node_module}/-/%{node_module}-%{version}.tgz

BuildArch:      noarch
BuildRequires:  rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs
Requires:       node rpm-build-nodejs

Provides:  nodejs-%node_module = %{version}-%{release}
Obsoletes: nodejs-%node_module < %version
Provides:  %node_module = %{version}-%{release}
Obsoletes: %node_module < %version

%description
TypeScript is a free and open source programming language developed by Microsoft.
 It is a strict superset of JavaScript, and essentially adds optional static 
typing and class-based object oriented programming to the language.
%prep
%setup -q -n package

%build

%check

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{nodejs_sitelib}/%{node_module}
chmod a+x bin/tsc
cp -rp bin package.json %{buildroot}/%{nodejs_sitelib}/%{node_module}

# Install /usr/bin/lessc
ln -s %{nodejs_sitelib}/%{node_module}/bin/tsc \
      %{buildroot}%{_bindir}

%nodejs_symlink_deps

%files
%doc CopyrightNotice.txt LICENSE.txt README.txt ThirdPartyNoticeText.txt
%{_bindir}/tsc
%{nodejs_sitelib}/%{node_module}

%changelog
* Sat Jul 27 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.9.0.1-alt1
Initial build
