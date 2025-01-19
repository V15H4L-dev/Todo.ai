import ReactDOM from "react-dom/client";
import App from "./App.tsx";
import { BrowserRouter } from "react-router-dom";
import { initColors } from "ntc-ts";
import { ORIGINAL_COLORS } from "ntc-ts";
import { UserContextProvider } from "./contexts/UserProvider.tsx";

// initialize ntc colors
initColors(ORIGINAL_COLORS);


// Listen for the `SKIP_WAITING` message and reload the page when the new SW takes over
navigator.serviceWorker?.addEventListener("controllerchange", () => {
  window.location.reload();
});

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <BrowserRouter>
    <UserContextProvider>
      <App />
    </UserContextProvider>
  </BrowserRouter>,
);
