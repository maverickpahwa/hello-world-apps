import { render, screen, waitFor } from "@testing-library/react";
import App from "./App";

// Mock the API response
global.fetch = jest.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve({ message: "Hello from Flask!" }),
  })
);

test("renders API response message", async () => {
  render(<App />);
  
  await waitFor(() => expect(screen.getByText(/Hello from Flask!/i)).toBeInTheDocument());
});
