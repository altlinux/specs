%global realname jose

%add_erlang_req_modules_skiplist Elixir.Atom
%add_erlang_req_modules_skiplist Elixir.Enum
%add_erlang_req_modules_skiplist Elixir.HashDict
%add_erlang_req_modules_skiplist Elixir.IO
%add_erlang_req_modules_skiplist Elixir.JOSE.Poison
%add_erlang_req_modules_skiplist Elixir.Kernel
%add_erlang_req_modules_skiplist Elixir.Map
%add_erlang_req_modules_skiplist Elixir.Poison
%add_erlang_req_modules_skiplist Elixir.Poison.EncodeError
%add_erlang_req_modules_skiplist Elixir.Poison.Encoder.Atom
%add_erlang_req_modules_skiplist Elixir.Poison.Encoder.BitString
%add_erlang_req_modules_skiplist Elixir.Poison.Encoder.Float
%add_erlang_req_modules_skiplist Elixir.Poison.Encoder.Integer
%add_erlang_req_modules_skiplist cutkey
%add_erlang_req_modules_skiplist jsone
%add_erlang_req_modules_skiplist jsx
%add_erlang_req_modules_skiplist keccakf1600
%add_erlang_req_modules_skiplist keccakf1600_fips202
%add_erlang_req_modules_skiplist libdecaf_curve25519
%add_erlang_req_modules_skiplist libdecaf_curve448
%add_erlang_req_modules_skiplist libdecaf_sha3
%add_erlang_req_modules_skiplist libsodium_crypto_aead_chacha20poly1305
%add_erlang_req_modules_skiplist libsodium_crypto_box_curve25519xsalsa20poly1305
%add_erlang_req_modules_skiplist libsodium_crypto_hash_sha512
%add_erlang_req_modules_skiplist libsodium_crypto_onetimeauth_poly1305
%add_erlang_req_modules_skiplist libsodium_crypto_scalarmult_curve25519
%add_erlang_req_modules_skiplist libsodium_crypto_sign_ed25519
%add_erlang_req_modules_skiplist libsodium_crypto_stream_chacha20
%add_erlang_req_modules_skiplist ojson

Name: erlang-%realname
Version: 1.8.4
Release: alt1%ubt
Summary: JSON Object Signing and Encryption (JOSE) for Erlang and Elixir
Group: Development/Erlang
License: MPLv2.0
BuildArch: noarch
Url: https://github.com/potatosalad/erlang-jose

# https://github.com/potatosalad/erlang-jose.git
Source: %name-%version.tar

Patch1: erlang-jose-fedora-use-include-instead-of-include_lib-for-jose-in-tests.patch
Patch2: erlang-jose-fedora-remove-warnings_as_errors-to-work-around-47.patch

BuildRequires(pre): rpm-build-erlang
BuildRequires(pre): rpm-build-ubt
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: rebar
BuildRequires: erlang-common_test-devel
BuildRequires: erlang-base64url
BuildRequires: erlang-triq

%description
JSON Object Signing and Encryption (JOSE) for Erlang and Elixir.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit -C rebar.test.config

%files
%doc LICENSE
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Tue Apr 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.4-alt1%ubt
- Initial build for ALT.
