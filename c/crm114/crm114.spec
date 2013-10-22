Name: crm114
Version: 1.0
Release: alt1

Summary: The Controllable Regex Mutilator
License: GPLv2
Group: Development/Other
Url: http://crm114.sourceforge.net/
Packager: Vladimir Didenko <cow@altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libtre-devel
BuildPreReq: emacs-devel
BuildRequires: emacs-common

%description
CRM114 is a system to examine incoming e-mail, system log streams,
data files or other data streams, and to sort, filter, or alter the
incoming files or data streams according to the user's wildest desires.
Criteria for categorization of data can be via a host of methods,
including regexes, approximate regexes, a Hidden Markov Model,
Bayesian Chain Rule Orthogonal Sparse Bigrams, Winnow, Correlation,
KNN/Hyperspace, Bit Entropy, CLUMP, SVM, Neural Networks
(or by other means- it's all programmable). 

%package samples
Summary: Sample programs for CRM114
License: GPLv3
Group: Development/Other
BuildArch: noarch

%description samples
This package provides sample programs for CRM114.

%package -n emacs-mode-%name
Summary: CRM114 mode for Emacs
Group: Editors
License: GPLv3
BuildArch: noarch

%description -n emacs-mode-%name
This package provides CRM114 mode for Emacs.

%prep
%setup -q 
%patch0 -p1

%build
%make_build

%install
%define prefix %buildroot/%_prefix
%define bindir %buildroot/%_bindir
%define datadir %buildroot%{_datadir}
%define _samplesdir %_datadir/%name/samples
%define samplesdir %buildroot/%_samplesdir
install -m755 -pd %bindir
install -m755 -pd %samplesdir

%makeinstall prefix=%prefix
cp *.crm %samplesdir

mkdir -p %buildroot%_emacslispdir/%name-mode/
install -m 644 %name-mode.el %buildroot%_emacslispdir/%name-mode/
%add_lisp_loadpath %buildroot%_emacslispdir/%name-mode
%byte_recompile_lispdir

%files
%_bindir/*
%dir %_datadir/%name
%doc *.txt

%files -n %name-samples
%_samplesdir

%files -n emacs-mode-%name
%dir %_emacslispdir/%name-mode/
%_emacslispdir/%name-mode/*.el*

%changelog
* Tue Oct 22 2013 Vladimir Didenko <cow@altlinux.org> 1.0-alt1
- Initial build for Sisyphus
