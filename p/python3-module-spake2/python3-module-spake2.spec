%define modulename spake2

Name: python3-module-spake2
Version: 0.7
Release: alt1

Summary: SPAKE2 password-authenticated key exchange (pure python)

Url: http://github.com/warner/python-spake2
License: MIT
Group: Development/Python

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://pypi.io/packages/source/s/%modulename/%modulename-%version.tar.gz
Source: %modulename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

%description
This library implements the SPAKE2 password-authenticated key exchange
("PAKE") algorithm. This allows two parties, who share a weak password, to
safely derive a strong shared secret (and therefore build an
encrypted+authenticated channel).

A passive attacker who eavesdrops on the connection learns no information
about the password or the generated secret. An active attacker
(man-in-the-middle) gets exactly one guess at the password, and unless they
get it right, they learn no information about the password or the generated
secret. Each execution of the protocol enables one guess. The use of a weak
password is made safer by the rate-limiting of guesses: no off-line
dictionary attack is available to the network-level attacker, and the
protocol does not depend upon having previously-established confidentiality
of the network (unlike e.g. sending a plaintext password over TLS).

The protocol requires the exchange of one pair of messages, so only one round
trip is necessary to establish the session key. If key-confirmation is
necessary, that will require a second round trip.

All messages are bytestrings. For the default security level (using the
Ed25519 elliptic curve, roughly equivalent to an 128-bit symmetric key), the
message is 33 bytes long.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info/

%changelog
* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- Initial build for ALT Sisyphus
